# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class VibrationMotorClient(Client):
    """
    A vibration motor.
    Implements a client for the `Vibration motor <https://microsoft.github.io/jacdac-docs/services/vibrationmotor>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_VIBRATION_MOTOR, JD_VIBRATION_MOTOR_PACK_FORMATS, role)


    @property
    def max_vibrations(self) -> Optional[int]:
        """
        (Optional) The maximum number of vibration sequences supported in a single packet., 
        """
        return self.register(JD_VIBRATION_MOTOR_REG_MAX_VIBRATIONS).value()

    
