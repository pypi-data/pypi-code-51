from dataclasses import dataclass
from typing import Dict

import numpy as np

from .basics import particularize
from .protocol_agent import protocol_agent
from .protocol_simulator import (JPGImage, protocol_simulator, RobotName, RobotObservations, RobotState,
                                 SetRobotCommands, StateDump)

__all__ = [
    "PWMCommands",
    "Duckiebot1Observations",
    "Duckiebot1Commands",
    "LEDSCommands",
    "RGB",
    "DB18SetRobotCommands",
    "DB18RobotObservations",
    "protocol_agent_duckiebot1",
    "protocol_simulator_duckiebot1",
    'DTSimRobotInfo', 'DTSimRobotState', 'DTSimState', 'DTSimStateDump'
]


@dataclass
class PWMCommands:
    """
        PWM commands are floats between -1 and 1.
    """

    motor_left: float
    motor_right: float

    def __post_init__(self):
        self.motor_left = float(self.motor_left)
        self.motor_right = float(self.motor_right)
        m = max(abs(self.motor_left), abs(self.motor_right))
        if m > 1:
            msg = f"Expected values to be between -1 and 1. Obtained {self.motor_left}, {self.motor_right}"
            raise ValueError(msg)


# @dataclass
# class WheelsCmd:
#     """ Kinematic wheels commands. Radiants per second. """
#     vel_left: float
#     vel_right: float


@dataclass
class Duckiebot1Observations:
    camera: JPGImage


@dataclass
class RGB:
    r: float
    g: float
    b: float

    def __post_init__(self):
        for a in [self.r, self.g, self.b]:
            if not isinstance(a, float):
                raise ValueError(a)


@dataclass
class LEDSCommands:
    center: RGB
    front_left: RGB
    front_right: RGB
    back_left: RGB
    back_right: RGB


@dataclass
class Duckiebot1Commands:
    wheels: PWMCommands
    LEDS: LEDSCommands


description = """Particularization for Duckiebot1 observations and commands."""
protocol_agent_duckiebot1 = particularize(
    protocol_agent,
    description=description,
    inputs={"observations": Duckiebot1Observations},
    outputs={"commands": Duckiebot1Commands},
)


@dataclass
class DB18SetRobotCommands(SetRobotCommands):
    robot_name: RobotName
    t_effective: float
    commands: Duckiebot1Commands


@dataclass
class DB18RobotObservations(RobotObservations):
    robot_name: RobotName
    t_effective: float
    observations: Duckiebot1Observations




@dataclass
class DTSimRobotInfo:
    pose: np.ndarray
    velocity: np.ndarray
    # last_action: np.ndarray[
    # wheels_velocities: np.ndarray
    pwm: PWMCommands
    leds: LEDSCommands


@dataclass
class DTSimRobotState(RobotState):
    robot_name: RobotName
    t_effective: float
    state: DTSimRobotInfo


@dataclass
class DTSimState:
    t_effective: float
    duckiebots: Dict[str, DTSimRobotInfo]


@dataclass
class DTSimStateDump(StateDump):
    state: DTSimState

description = """Particularization for Duckiebot1 observations and commands."""
protocol_simulator_duckiebot1 = particularize(
    protocol_simulator,
    description=description,
    inputs={"set_robot_commands": DB18SetRobotCommands},
    outputs={"robot_observations": DB18RobotObservations,
            "robot_state": DTSimRobotState,
            'state_dump': DTSimStateDump
    },
)
