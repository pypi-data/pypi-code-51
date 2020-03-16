# Copyright 2019 Tobias Höfer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""The code is written using the Keras Sequential API with a tf.GradientTape
training loop. This module implements the minmax game used to train a GAN.

Generative Adversarial Networks (GANs) are one of the most interesting ideas in
computer science today. Two models are trained simultaneously by an adversarial
process. A generator("the artist") learns to create images that look real, while
a discriminator ("the art critic") learns to tell real images apart from fakes.

Original paper: https://arxiv.org/abs/1406.2661

Two players
-----------
The two player in the game are represented by two functions, each of which is
differentiable both with respect to its inputs and with respect to its
parameters. Both players have loss functions that are defined in terms of both
players' parameters. The discriminator takes x as input and uses θ_D as
parameters. The generator is defined by a function g that takes z as input and
uses θ_G as parameters. Because each player's cost depends on the other player's
parameters, but each player cannot control the other player's parameters, this
scenario is most straightforward to describe as a game rather than as an
optimization problem. The solution to an optimization problem is a local minimum
, a point in parameters space where all neighboring points have greater or equal
cost. The solution to a game is a Nash equilibrium. Here, we use the terminology
of local differential Nash equilibria. In this context, a Nash equilibriom is a
tuple (θ_D, θ_G) that is a local minimum of both loss functions with respect
to their corresponding parameters θ.

The generator G (primary model):        x = G(z;θ_G)
--------------------------------
    - any kind of differentiable function that has parameters that we can learn
      with gradient descent. Usually a neural network as in the original paper.
    - tries to capture the input data distribution.
    - beginn by sampling the latent vector Z from the prior distriution
      (e.g a normal distribution) over latent variables, so Z is essentially a
      vector of unstructured noise, it's a source of randomness that allows the
      generator to output a wide variety of different vectors.
    - the generator then maps z to the data space x = G(z;θ)
    - trainable for any size of z. If we want p_model to have full support on
      x space we need the dimension of z to be at least as large as the
      dimension of x.
    - ancestral sampling (forward sampling): Main reason that GANs are
      simple to train is that we never actually try to infer the
      probability distribution over Z given X, instead we sample values z
      from the prior and then we sample values of x from P(x|z)
    - can make x conditionally Gaussian given z but need not do so.

    => Train G to minimize the log probability of the discriminator being
       correct: log(1 - D(G(z))).

The discriminator D (not really neccessary after the training process):
-----------------------------------------------------------------------
    - any kind of differentiable function that has parameters that we can learn
      with gradient descent. A neural network is used in the original paper.
    - estimates the probability that samples come from the data distribution
      rather than from G.
    - apply the discriminator to real images and its goal is to output a value
      that is near 1 representing a high probability that the input was real
      rather than fake but half the time we also apply the discriminator to
      examples that are in fact fake (generated by the generator). In this case
      the discriminator tries to output a value close to 0 representing a low
      probability that the input was real.
    - outputs a single scalar [0, 1]
    - learns using traditional supervised learning, dividing inputs into two
      classes (real or fake)

    => Train to maximize the probability of assigning the correct label to both
       data samples and samples from G(z).


Minimax game (Theory)
---------------------
Define a cost for the discriminator and the cost for the generator is negative
of the cost for the discriminator. Think of a single value that the
discriminator is trying to maximize and the generator is trying to minimize. The
value that the two players are fighting over is the cross-entropy between the
discriminators predictions and the correct labels in the binary classification
task of discriminating real data from fake data.

Both players are trained simultaneously playing the following minimax game:
    J_D = E_x_from_data [log(D(x))] + E_z_from_generator [log(1-D(G(z)))]
           "Detect real images"              "Detect fake images"
                [-∞, 0]                             [-∞, 0]

    J_G = - J_D

- discriminator tries to maximize J_D.
- generator tries to minimize J_D.
- equilibrium is a saddle point of the discriminator loss.
- resembles Jensen-Shannon divergence.
- generator minimizes the log-probability of the discriminator being correct:
  log(1-D(G(z)))

!!! Early in learning, when G(z) produces poor outputs, D can reject with high
confidence. In this case log(1-D(G(z))) saturates.


Non-Saturating Game (Practise)
------------------------------
Each player has its own independently parameterised cost function to eliminate
early saturation due to a dominant discriminator. Heuristically motivated; the
generator can still learn even when discriminator successfully rejects all
generator samples.

Generator maximizes the log-probability of the discriminator being mistaken:
    max D(G(z))

instead of minimizing the minmax game.

This term is simply being copied from the original loss function.


Training procedure
------------------
On each step, two minibatches are sampled:
    - a minibatch of training examples.
    - a minibatch of generated samples.
Use SGD-like algorithm of choice (default:Adam) on two players
simultaneously.

Optional: run k steps of one player for every step of the other player.
          I personally usually use one update for each player (k=1).


Training heuristics (hacks)
---------------------------
- normalize inputs to -1 and 1.
- use tanh in combination with normalized inputs.
- avoid sparse gradients, use leakyReLU
- Don't sample from a Uniform distribution (z), sample from a gaussian dist.
  When doing interpolations, do the interpolation via a freat circle, rather
  than a straight line form point A to point B.
- Different mini-batches for real and fake.
- use the ADAM optimizer.
- if Discriminator loss shows low variance and decreases over time the training
  is working. If loss of generator steadily decreases, then its fooling the D
  with garbage.
- training fails if discriminator loss equals 0 or norms of generator gradients
  are greater 100.
"""
import logging
import os
import time
from datetime import datetime

import tensorflow as tf
from dnnlab.errors.dnnlab_exceptions import ModelNotCompiledError

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # FATAL
logging.getLogger("tensorflow").setLevel(logging.FATAL)


class GAN(object):
    """Implements a generative adversarial net (GAN) learning model.

        Typical usage example:

        generator -> keras.model with input layer = z_dims & output same dim
                     than data examples.
        discriminator -> keras.model with input layer = dim data examples &
                         outputs a single scalar (1 neuron).

        # Define forward path.
        gan = GAN(generator, discriminator, z_dims=100)

        # Define optimizer.
        gan.compile(lr_gen=1e-4, lr_disc=1e-4)

        # Start training process.
        gan.fit(dataset, EPOCHS, BATCH_SIZE, save_ckpt=5)

        # Export both models.
        gan.export()

        use gan.restore("relative_path_to_logs") to continue training after
        a break.


    Attributes:
        generator (keras.model): Keras NN to act as the generator.
        discriminator (keras.model): Keras NN to act as the discriminator.
        z_dim (int): Dimension of input latent noise variables to generator.
        generator_optimizer (keras.optimizer): Optimization alg for generator.
        discriminator_optimizer (keras.optimizer): Optimization alg for disc.
        init_timestamp (str): Acts as a unique folder identifier.
        logdir (str): Top level logdir.
        tensorboard (str): Path to tensorboard summary files.
        ckpt_dir (str): Path to ckpt files.
        ckpt_manager (tf.train.CheckpointManager): Deletes old checkpoints.
        checkpoint (tf.train.Checkpoint): Groups trackable objects, saving and
            restoring them.
    """
    def __init__(self, generator, discriminator, z_dim=100):
        """Takes two keras.models that take part in the minmax game.
        Both models define the hypothesis set to our learning model.

        Args:
            generator (keras.model): Keras NN to act as the generator.
            discriminator (keras.model): Keras NN to act as the discriminator.
            z_dim (int): Number of input latent noise variables to generator.
        """
        self.generator = generator
        self.discriminator = discriminator
        self.z_dim = z_dim
        self.generator_optimizer = None
        self.discriminator_optimizer = None
        self.init_timestamp = "GAN-" + datetime.now().strftime("%d%m%Y-%H%M%S")
        self.logdir = os.path.join("logs", self.init_timestamp)
        self.tensorboard = os.path.join(self.logdir, "tensorboard")
        self.ckpt_dir = os.path.join(self.logdir, "ckpts")
        self.ckpt_manager = None
        self.checkpoint = None

    def compile(self, optimizer="adam", lr_gen=1e-4, lr_disc=1e-4):
        """Defines the optimization part of the learning algorithm to our
        learning model.

        Args:
            optimizer (str, optional): Optimizer. Defaults to "adam".
            lr_gen (Float, optional): Learning rate generator. Defaults to 1e4.
            lr_disc (Float, optional): Learning rate discriminator.
                Defaults to 1e4.
        """
        # TODO: more optimizer
        if optimizer == "adam":
            self.generator_optimizer = tf.keras.optimizers.Adam(lr_gen)
            self.discriminator_optimizer = tf.keras.optimizers.Adam(lr_disc)

        if self.checkpoint is None:
            self.checkpoint = tf.train.Checkpoint(
                generator_optimizer=self.generator_optimizer,
                discriminator_optimizer=self.discriminator_optimizer,
                generator=self.generator,
                discriminator=self.discriminator)
            self.ckpt_manager = tf.train.CheckpointManager(self.checkpoint,
                                                           self.ckpt_dir,
                                                           max_to_keep=5)

    def fit(self,
            dataset,
            epochs,
            batch_size,
            save_ckpt=5,
            verbose=1,
            max_outputs=2,
            initial_step=0):
        """Trains both models for n EPOCHS. Saves ckpts every n EPOCHS.
        The training loop together with the optimization algorithm define the
        learning algorithm.

        Args:
            dataset (tf.dataset): tf.Dataset with
                shape(None, width, height, depth).
            epochs (int): Number of epochs.
            batch_size (int): Batch length.
            save_ckpt (int): Save ckpts every n Epochs.
            verbose (int, optional): Keras Progbar verbose lvl. Defaults to 1.
            max_outputs (int, optional): Number of images shown in TB.
                Defaults to 2.
            initial_step (int): Step at which to start training. Useful for
                resuming a previous run.


        Raises:
            ModelNotCompiledError: Raise if model is not compiled.
        """
        if self.generator_optimizer is None:
            raise ModelNotCompiledError("use GAN.compile() first.")

        # Retrace workaround @function signature only tensors.
        step = tf.Variable(initial_step, name="step", dtype=tf.int64)

        num_batches = tf.data.experimental.cardinality(dataset).numpy()
        # Keras Progbar
        progbar = tf.keras.utils.Progbar(target=num_batches, verbose=verbose)
        file_writer = tf.summary.create_file_writer(self.tensorboard)
        file_writer.set_as_default()
        for epoch in range(epochs):
            step_float = 0
            start = time.time()
            for image_batch in dataset:
                self.train_step(image_batch, batch_size, step, max_outputs,
                                file_writer)
                file_writer.flush()
                progbar.update(current=(step_float))
                step_float += 1
                step.assign(step + 1)

            # Save the model every n epochs
            if (epoch + 1) % save_ckpt == 0:
                ckpt_save_path = self.ckpt_manager.save()
                print("\nSaving checkpoint for epoch {} at {}".format(
                    epoch + 1, ckpt_save_path))

            print(" - Epoch {} finished in {} sec\n".format(
                epoch + 1, int(time.time() - start)))

    def restore(self, ckpt_path):
        """Restore model weights from the latest checkpoint.

        Args:
            ckpt_path (str): Relative path to ckpt files.

        Raises:
            ModelNotCompiledError: Raise if model is not compiled.
        """

        restore_path = os.path.dirname(ckpt_path)
        self.logdir = restore_path
        self.tensorboard = os.path.join(self.logdir, "tensorboard")
        self.ckpt_dir = os.path.join(self.logdir, "ckpts")
        if self.ckpt_manager is None:
            raise ModelNotCompiledError("use GAN.compile() first.")
        self.ckpt_manager = tf.train.CheckpointManager(self.checkpoint,
                                                       self.ckpt_dir,
                                                       max_to_keep=5)
        # if a checkpoint exists, restore the latest checkpoint.
        if self.ckpt_manager.latest_checkpoint:
            self.checkpoint.restore(self.ckpt_manager.latest_checkpoint)
            print("Latest checkpoint restored!!")
        else:
            print("Can not find ckpt files at {}".format(ckpt_path))

    def export(self, model_format="hdf5"):
        """Exports the trained models in hdf5 or SavedModel format.

        Args:
            model_format (str, optional): SavedModel or HDF5. Defaults to hdf5.
        """
        model_dir = os.path.join(self.logdir, "models")
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)

        if model_format == "hdf5":
            self.generator.save(os.path.join(model_dir, "generator.h5"))
            self.discriminator.save(os.path.join(model_dir,
                                                 "discriminator.h5"))

        elif model_format == "SavedModel":
            self.generator.save(os.path.join(model_dir, "generator"))
            self.discriminator.save(os.path.join(model_dir, "discriminator"))

    @tf.function
    def train_step(self, real_images, batch_size, step, max_outputs,
                   file_writer):
        """Decorated function (@tf.function) that creates a callable tensorflow
        graph from a python function.
        """
        # TODO(Tobi): Trace keras.models graph to visualize in tensorboard.
        with file_writer.as_default():
            z_latent = tf.random.normal([batch_size, self.z_dim])
            # Record gradients for generator and discriminator for each seperate
            # training step.
            with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
                generated_images = self.generator(z_latent, training=True)
                tf.summary.image("generated_images",
                                 generated_images,
                                 max_outputs=max_outputs,
                                 step=step)
                tf.summary.image("real_images",
                                 real_images,
                                 max_outputs=max_outputs,
                                 step=step)

                real_output = self.discriminator(real_images, training=True)
                fake_output = self.discriminator(generated_images,
                                                 training=True)

                gen_loss = self.generator_loss(fake_output)
                tf.summary.scalar("generator_loss", gen_loss, step=step)

                disc_loss = self.discriminator_loss(real_output, fake_output)
                tf.summary.scalar("discriminator_loss", disc_loss, step=step)

            gradients_of_generator = gen_tape.gradient(
                gen_loss, self.generator.trainable_variables)

            # Compute the euclidean vector norm L2 for the gradients of the
            # generator.
            # GradientTape.gradient() returns a list of Tensors, one for each
            # element in sources. Returned structure is the same as the
            # structure of sources.
            gradient_norm_generator = tf.linalg.global_norm(
                gradients_of_generator)
            tf.summary.scalar("gen_gradient_norm_l2",
                              gradient_norm_generator,
                              step=step)
            gradients_of_discriminator = disc_tape.gradient(
                disc_loss, self.discriminator.trainable_variables)
            # Compute the euclidean vector norm L2 for the gradients of the
            # discriminator.
            gradient_norm_discriminator = tf.linalg.global_norm(
                gradients_of_discriminator)
            tf.summary.scalar("disc_gradient_norm_l2",
                              gradient_norm_discriminator,
                              step=step)

            self.generator_optimizer.apply_gradients(
                zip(gradients_of_generator,
                    self.generator.trainable_variables))
            self.discriminator_optimizer.apply_gradients(
                zip(gradients_of_discriminator,
                    self.discriminator.trainable_variables))

    @staticmethod
    def discriminator_loss(real_output, fake_output):
        """This method quantifies how well the discriminator is able to
        distinguish real images from fakes. It compares the discriminator's
        predictions on real images to an array of 1s, and the discriminator's
        predictions on fake (generated) images to an array of 0s.

        Args:
            real_output: Prob. array of discriminator's performance on real data
            fake_output: Prob. array of discriminator's performance on fake data
        """
        # This method returns a helper function to compute cross entropy loss.
        cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
        # Compares real images to tensors of 1 -> if real output 1s
        real_loss = cross_entropy(tf.ones_like(real_output), real_output)
        # Compares generated images to tensors of 0 -> if generated output 0s
        fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)

        total_loss = real_loss + fake_loss
        return total_loss

    @staticmethod
    def generator_loss(fake_output):
        """The generator's loss quantifies how well it was able to trick the
           discriminator. Intuitively, if the generator is performing well, the
           discriminator will classify the generated images as real (or 1).
           Here, we will compare the discriminators decisions on the generated
           images to an array of 1s.

        Args:
            fake_output: Prob. array of discriminator's performance on fake data
        """
        # This method returns a helper function to compute cross entropy loss.
        cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
        return cross_entropy(tf.ones_like(fake_output), fake_output)
