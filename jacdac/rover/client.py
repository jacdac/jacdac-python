# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional, Tuple


class RoverClient(SensorClient):
    """
    A roving robot.
    Implements a client for the `Rover <https://microsoft.github.io/jacdac-docs/services/rover>`_ service.

    """

    def __init__(self, bus: Bus, role: str, *, missing_kinematics_value: Tuple[float, float, float, float, float] = None) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_ROVER, JD_ROVER_PACK_FORMATS, role)
        self.missing_kinematics_value = missing_kinematics_value

    @property
    def kinematics(self) -> Optional[Tuple[float, float, float, float, float]]:
        """
        The current position and orientation of the robot., x: cm,y: cm,vx: cm/s,vy: cm/s,heading: °
        """
        self.refresh_reading()
        return self.register(JD_ROVER_REG_KINEMATICS).value(self.missing_kinematics_value)

    
