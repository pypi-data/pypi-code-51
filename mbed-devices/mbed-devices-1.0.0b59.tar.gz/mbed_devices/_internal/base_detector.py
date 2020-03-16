"""Interface for device detectors."""
from abc import ABC, abstractmethod
from typing import List

from mbed_devices._internal.candidate_device import CandidateDevice


class DeviceDetector(ABC):
    """Object in charge of finding USB devices."""

    @abstractmethod
    def find_candidates(self) -> List[CandidateDevice]:
        """Returns CandidateDevices."""
        pass
