# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class SolenoidClient(Client):
    """
    A push-pull solenoid is a type of relay that pulls a coil when activated.
    Implements a client for the `Solenoid <https://microsoft.github.io/jacdac-docs/services/solenoid>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_SOLENOID, JD_SOLENOID_PACK_FORMATS, role)


    @property
    def pulled(self) -> Optional[bool]:
        """
        Indicates whether the solenoid is energized and pulled (on) or pushed (off)., 
        """
        return self.register(JD_SOLENOID_REG_PULLED).bool_value()

    @pulled.setter
    def pulled(self, value: bool) -> None:
        self.register(JD_SOLENOID_REG_PULLED).set_values(value)


    @property
    def variant(self) -> Optional[SolenoidVariant]:
        """
        (Optional) Describes the type of solenoid used., 
        """
        return self.register(JD_SOLENOID_REG_VARIANT).value()

    
