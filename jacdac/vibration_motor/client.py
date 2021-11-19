# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class VibrationMotorClient(Client):
    """
    A vibration motor.
    Implements a client for the `Vibration motor <https://microsoft.github.io/jacdac-docs/services/vibration>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_VIBRATION_MOTOR, JD_VIBRATION_MOTOR_PACK_FORMATS, role)
    

    @property
    def enabled(self) -> Optional[bool]:
        """
        Determines if the vibration motor responds to vibrate commands., 
        """
        return self.register(JD_VIBRATION_MOTOR_REG_ENABLED).value()

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self.register(JD_VIBRATION_MOTOR_REG_ENABLED).set_values(value)


    
