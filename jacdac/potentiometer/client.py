# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class PotentiometerClient(SensorClient):
    """
    A slider or rotary potentiometer.
    Implements a client for the `Potentiometer <https://microsoft.github.io/jacdac-docs/services/potentiometer>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_POTENTIOMETER, JD_POTENTIOMETER_PACK_FORMATS, role)
    

    @property
    def position(self) -> Optional[float]:
        """
        The relative position of the slider., _: /
        """
        self.refresh_reading()
        return self.register(JD_POTENTIOMETER_REG_POSITION).float_value(100)

    @property
    def variant(self) -> Optional[PotentiometerVariant]:
        """
        (Optional) Specifies the physical layout of the potentiometer., 
        """
        return self.register(JD_POTENTIOMETER_REG_VARIANT).value()

    
