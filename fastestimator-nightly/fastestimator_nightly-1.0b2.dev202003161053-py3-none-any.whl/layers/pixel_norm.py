# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
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
import tensorflow as tf
from tensorflow.keras import layers


class PixelNormalization(layers.Layer):
    """ This layer normalizes each pixel by its L2-norm along the channel axis divided by the number of channels.

    Args:
        eps (float, optional): epsilon parameter which defaults to 1e-8
    """
    def __init__(self, eps=1e-8):
        super().__init__()
        self.eps = eps

    def get_config(self):
        return {'eps': self.eps}

    def call(self, inputs):
        return inputs * tf.math.rsqrt(tf.reduce_mean(tf.square(inputs), axis=-1, keepdims=True) + self.eps)
