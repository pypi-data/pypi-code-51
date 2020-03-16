# coding=utf-8
# Copyright 2018 The TF-Agents Authors.
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


# Changes:
#
#  - 2019/12/09 JD: inline and remove tensorflow dependency/shape support
#  - 2019/12/11 JD: add MathyObservation type hints
"""TimeStep representing a step in the environment.

This file is a mostly direct copy of the implementation from the
[tf_agents](https://github.com/tensorflow/agents) library but has
the dependency on tensorflow removed along with advanced shape
features.

Mathy doesn't use these features and the overhead of loading tensorflow
to pass environment states around is not great for things like CLI start
times.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import numpy as np


class TimeStep(
    collections.namedtuple(
        "TimeStep", ["step_type", "reward", "discount", "observation"]
    )
):
    __slots__ = ()

    def is_first(self):
        return np.equal(self.step_type, StepType.FIRST)

    def is_mid(self):
        return np.equal(self.step_type, StepType.MID)

    def is_last(self):
        return np.equal(self.step_type, StepType.LAST)

    def __hash__(self):
        return hash(tuple(self))


class StepType(object):
    """Defines the status of a `TimeStep` within a sequence."""

    # Denotes the first `TimeStep` in a sequence.
    FIRST = np.asarray(0, dtype=np.int32)
    # Denotes any `TimeStep` in a sequence that is not FIRST or LAST.
    MID = np.asarray(1, dtype=np.int32)
    # Denotes the last `TimeStep` in a sequence.
    LAST = np.asarray(2, dtype=np.int32)

    def __new__(cls, value):
        """Add ability to create StepType constants from a value."""
        if value == cls.FIRST:
            return cls.FIRST
        if value == cls.MID:
            return cls.MID
        if value == cls.LAST:
            return cls.LAST

        raise ValueError("No known conversion for `%r` into a StepType" % value)


def transition(observation, reward, discount=1.0):
    """Returns a `TimeStep` with `step_type` set equal to `StepType.MID`."""
    return TimeStep(StepType.MID, reward, discount, observation)


def termination(observation, reward):
    """Returns a `TimeStep` with `step_type` set to `StepType.LAST`."""
    return TimeStep(StepType.LAST, reward, 00, observation)


def truncation(observation, reward, discount=1.0):
    """Returns a `TimeStep` with `step_type` set to `StepType.LAST`."""
    return TimeStep(StepType.LAST, reward, discount, observation)
