# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class ServoClient(Client):
    """
    Servo is a small motor with arm that can be pointing at a specific direction.
     * 
     * The `min/max_angle/pulse` may be read-only if the servo is permanently affixed to its Jacdac controller.
    Implements a client for the `Servo <https://microsoft.github.io/jacdac-docs/services/servo>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_SERVO, JD_SERVO_PACK_FORMATS, role)
    

    @property
    def angle(self) -> Optional[float]:
        """
        Specifies the angle of the arm (request)., _: °
        """
        return self.register(JD_SERVO_REG_ANGLE).value()

    @angle.setter
    def angle(self, value: float) -> None:
        self.enabled = True
        self.register(JD_SERVO_REG_ANGLE).set_values(value)


    @property
    def enabled(self) -> Optional[bool]:
        """
        Turn the power to the servo on/off., 
        """
        return self.register(JD_SERVO_REG_ENABLED).value()

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self.register(JD_SERVO_REG_ENABLED).set_values(value)


    @property
    def offset(self) -> Optional[float]:
        """
        Correction applied to the angle to account for the servo arm drift., _: °
        """
        return self.register(JD_SERVO_REG_OFFSET).value()

    @offset.setter
    def offset(self, value: float) -> None:
        self.register(JD_SERVO_REG_OFFSET).set_values(value)


    @property
    def min_angle(self) -> Optional[float]:
        """
        Lowest angle that can be set., _: °
        """
        return self.register(JD_SERVO_REG_MIN_ANGLE).value()

    @property
    def min_pulse(self) -> Optional[int]:
        """
        The length of pulse corresponding to lowest angle., _: us
        """
        return self.register(JD_SERVO_REG_MIN_PULSE).value()

    @min_pulse.setter
    def min_pulse(self, value: int) -> None:
        self.register(JD_SERVO_REG_MIN_PULSE).set_values(value)


    @property
    def max_angle(self) -> Optional[float]:
        """
        Highest angle that can be set., _: °
        """
        return self.register(JD_SERVO_REG_MAX_ANGLE).value()

    @property
    def max_pulse(self) -> Optional[int]:
        """
        The length of pulse corresponding to highest angle., _: us
        """
        return self.register(JD_SERVO_REG_MAX_PULSE).value()

    @max_pulse.setter
    def max_pulse(self, value: int) -> None:
        self.register(JD_SERVO_REG_MAX_PULSE).set_values(value)


    @property
    def stall_torque(self) -> Optional[float]:
        """
        (Optional) The servo motor will stop rotating when it is trying to move a ``stall_torque`` weight at a radial distance of ``1.0`` cm., _: kg/cm
        """
        return self.register(JD_SERVO_REG_STALL_TORQUE).value()

    @property
    def response_speed(self) -> Optional[float]:
        """
        (Optional) Time to move 60°., _: s/60°
        """
        return self.register(JD_SERVO_REG_RESPONSE_SPEED).value()

    @property
    def current_angle(self) -> Optional[float]:
        """
        (Optional) The current physical position of the arm., _: °
        """
        return self.register(JD_SERVO_REG_CURRENT_ANGLE).value()

    
