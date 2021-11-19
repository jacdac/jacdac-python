# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class FlexClient(SensorClient):
    """
    A bending or deflection sensor.
    Implements a client for the `Flex <https://microsoft.github.io/jacdac-docs/services/flex>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_FLEX, JD_FLEX_PACK_FORMATS, role)
    

    @property
    def bending(self) -> Optional[float]:
        """
        The relative position of the slider., _: /
        """
        self.refresh_reading()
        return self.register(JD_FLEX_REG_BENDING).float_value(100)

    @property
    def variant(self) -> Optional[FlexVariant]:
        """
        (Optional) Specifies the physical layout of the flex sensor., 
        """
        return self.register(JD_FLEX_REG_VARIANT).value()

    
