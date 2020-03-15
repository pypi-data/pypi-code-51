# MIT License
#
# Copyright (C) IBM Corporation 2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This module implements adversarial training based on a model and one or multiple attack methods. It incorporates
original adversarial training, ensemble adversarial training, training on all adversarial data and other common setups.
If multiple attacks are specified, they are rotated for each batch. If the specified attacks have as target a different
model, then the attack is transferred. The `ratio` determines how many of the clean samples in each batch are replaced
with their adversarial counterpart.

.. warning:: Both successful and unsuccessful adversarial samples are used for training. In the case of
              unbounded attacks (e.g., DeepFool), this can result in invalid (very noisy) samples being included.

| Paper link: https://arxiv.org/abs/1705.07204

| Please keep in mind the limitations of defences. While adversarial training is widely regarded as a promising,
    principled approach to making classifiers more robust (see https://arxiv.org/abs/1802.00420), very careful
    evaluations are required to assess its effectiveness case by case (see https://arxiv.org/abs/1902.06705).
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

import numpy as np

from art.defences.trainer.trainer import Trainer

logger = logging.getLogger(__name__)


class AdversarialTrainer(Trainer):
    """
    Class performing adversarial training based on a model architecture and one or multiple attack methods.

    Incorporates original adversarial training, ensemble adversarial training (https://arxiv.org/abs/1705.07204),
    training on all adversarial data and other common setups. If multiple attacks are specified, they are rotated
    for each batch. If the specified attacks have as target a different model, then the attack is transferred. The
    `ratio` determines how many of the clean samples in each batch are replaced with their adversarial counterpart.

     .. warning:: Both successful and unsuccessful adversarial samples are used for training. In the case of
                  unbounded attacks (e.g., DeepFool), this can result in invalid (very noisy) samples being included.

    | Paper link: https://arxiv.org/abs/1705.07204

    | Please keep in mind the limitations of defences. While adversarial training is widely regarded as a promising,
        principled approach to making classifiers more robust (see https://arxiv.org/abs/1802.00420), very careful
        evaluations are required to assess its effectiveness case by case (see https://arxiv.org/abs/1902.06705).
    """

    def __init__(self, classifier, attacks, ratio=0.5):
        """
        Create an :class:`.AdversarialTrainer` instance.

        :param classifier: Model to train adversarially.
        :type classifier: :class:`.Classifier`
        :param attacks: attacks to use for data augmentation in adversarial training
        :type attacks: :class:`.EvasionAttack` or `list(EvasionAttack)`
        :param ratio: The proportion of samples in each batch to be replaced with their adversarial counterparts.
                      Setting this value to 1 allows to train only on adversarial samples.
        :type ratio: `float`
        """
        from art.attacks import EvasionAttack

        self.classifier = classifier
        if isinstance(attacks, EvasionAttack):
            self.attacks = [attacks]
        elif isinstance(attacks, list):
            self.attacks = attacks
        else:
            raise ValueError("Only EvasionAttack instances or list of attacks supported.")

        if ratio <= 0 or ratio > 1:
            raise ValueError("The `ratio` of adversarial samples in each batch has to be between 0 and 1.")
        self.ratio = ratio

        self._precomputed_adv_samples = []
        self.x_augmented, self.y_augmented = None, None

    def fit_generator(self, generator, nb_epochs=20, **kwargs):
        """
        Train a model adversarially using a data generator.
        See class documentation for more information on the exact procedure.

        :param generator: Data generator.
        :type generator: :class:`.DataGenerator`
        :param nb_epochs: Number of epochs to use for trainings.
        :type nb_epochs: `int`
        :param kwargs: Dictionary of framework-specific arguments. These will be passed as such to the `fit` function of
               the target classifier.
        :type kwargs: `dict`
        :return: `None`
        """
        logger.info("Performing adversarial training using %i attacks.", len(self.attacks))
        size = generator.size
        batch_size = generator.batch_size
        nb_batches = int(np.ceil(size / batch_size))
        ind = np.arange(generator.size)
        attack_id = 0

        # Precompute adversarial samples for transferred attacks
        logged = False
        self._precomputed_adv_samples = []
        for attack in self.attacks:
            if "targeted" in attack.attack_params:
                if attack.targeted:
                    raise NotImplementedError("Adversarial training with targeted attacks is currently not implemented")

            if attack.classifier != self.classifier:
                if not logged:
                    logger.info("Precomputing transferred adversarial samples.")
                    logged = True

                next_precomputed_adv_samples = None
                for batch_id in range(nb_batches):
                    # Create batch data
                    x_batch, y_batch = generator.get_batch()
                    x_adv_batch = attack.generate(x_batch, y=y_batch)
                    if next_precomputed_adv_samples is None:
                        next_precomputed_adv_samples = x_adv_batch
                    else:
                        next_precomputed_adv_samples = np.append(next_precomputed_adv_samples, x_adv_batch, axis=0)
                self._precomputed_adv_samples.append(next_precomputed_adv_samples)
            else:
                self._precomputed_adv_samples.append(None)

        for i_epoch in range(nb_epochs):
            logger.info("Adversarial training epoch %i/%i", i_epoch, nb_epochs)

            # Shuffle the indices of precomputed examples
            np.random.shuffle(ind)

            for batch_id in range(nb_batches):
                # Create batch data
                x_batch, y_batch = generator.get_batch()
                x_batch = x_batch.copy()

                # Choose indices to replace with adversarial samples
                nb_adv = int(np.ceil(self.ratio * x_batch.shape[0]))
                attack = self.attacks[attack_id]
                if self.ratio < 1:
                    adv_ids = np.random.choice(x_batch.shape[0], size=nb_adv, replace=False)
                else:
                    adv_ids = list(range(x_batch.shape[0]))
                    np.random.shuffle(adv_ids)

                # If source and target models are the same, craft fresh adversarial samples
                if attack.classifier == self.classifier:
                    x_batch[adv_ids] = attack.generate(x_batch[adv_ids], y=y_batch[adv_ids])

                # Otherwise, use precomputed adversarial samples
                else:
                    x_adv = self._precomputed_adv_samples[attack_id]
                    x_adv = x_adv[ind[batch_id * batch_size : min((batch_id + 1) * batch_size, size)]][adv_ids]
                    x_batch[adv_ids] = x_adv

                # Fit batch
                self.classifier.fit(x_batch, y_batch, nb_epochs=1, batch_size=x_batch.shape[0], **kwargs)
                attack_id = (attack_id + 1) % len(self.attacks)

    def fit(self, x, y, validation_data=None, batch_size=128, nb_epochs=20, **kwargs):
        """
        Train a model adversarially. See class documentation for more information on the exact procedure.

        :param x: Training set.
        :type x: `np.ndarray`
        :param y: Labels for the training set.
        :type y: `np.ndarray`
        :param batch_size: Size of batches.
        :type batch_size: `int`
        :param nb_epochs: Number of epochs to use for trainings.
        :type nb_epochs: `int`
        :param kwargs: Dictionary of framework-specific arguments. These will be passed as such to the `fit` function of
               the target classifier.
        :type kwargs: `dict`
        :return: `None`
        """
        logger.info("Performing adversarial training using %i attacks.", len(self.attacks))
        nb_batches = int(np.ceil(len(x) / batch_size))
        ind = np.arange(len(x))
        attack_id = 0

        # Precompute adversarial samples for transferred attacks
        logged = False
        self._precomputed_adv_samples = []
        for attack in self.attacks:
            if "targeted" in attack.attack_params:
                if attack.targeted:
                    raise NotImplementedError("Adversarial training with targeted attacks is currently not implemented")

            if attack.classifier != self.classifier:
                if not logged:
                    logger.info("Precomputing transferred adversarial samples.")
                    logged = True
                self._precomputed_adv_samples.append(attack.generate(x, y=y))
            else:
                self._precomputed_adv_samples.append(None)

        for i_epoch in range(nb_epochs):
            logger.info("Adversarial training epoch %i/%i", i_epoch, nb_epochs)

            # Shuffle the examples
            np.random.shuffle(ind)

            for batch_id in range(nb_batches):
                # Create batch data
                x_batch = x[ind[batch_id * batch_size : min((batch_id + 1) * batch_size, x.shape[0])]].copy()
                y_batch = y[ind[batch_id * batch_size : min((batch_id + 1) * batch_size, x.shape[0])]]

                # Choose indices to replace with adversarial samples
                nb_adv = int(np.ceil(self.ratio * x_batch.shape[0]))
                attack = self.attacks[attack_id]
                if self.ratio < 1:
                    adv_ids = np.random.choice(x_batch.shape[0], size=nb_adv, replace=False)
                else:
                    adv_ids = list(range(x_batch.shape[0]))
                    np.random.shuffle(adv_ids)

                # If source and target models are the same, craft fresh adversarial samples
                if attack.classifier == self.classifier:
                    x_batch[adv_ids] = attack.generate(x_batch[adv_ids], y=y_batch[adv_ids])

                # Otherwise, use precomputed adversarial samples
                else:
                    x_adv = self._precomputed_adv_samples[attack_id]
                    x_adv = x_adv[ind[batch_id * batch_size : min((batch_id + 1) * batch_size, x.shape[0])]][adv_ids]
                    x_batch[adv_ids] = x_adv

                # Fit batch
                self.classifier.fit(x_batch, y_batch, nb_epochs=1, batch_size=x_batch.shape[0], **kwargs)
                attack_id = (attack_id + 1) % len(self.attacks)

    def predict(self, x, **kwargs):
        """
        Perform prediction using the adversarially trained classifier.

        :param x: Test set.
        :type x: `np.ndarray`
        :param kwargs: Other parameters to be passed on to the `predict` function of the classifier.
        :type kwargs: `dict`
        :return: Predictions for test set.
        :rtype: `np.ndarray`
        """
        return self.classifier.predict(x, **kwargs)
