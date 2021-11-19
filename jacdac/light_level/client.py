# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class LightLevelClient(Client):
    """
    A sensor that measures luminosity level.
    Implements a client for the `Light level <https://microsoft.github.io/jacdac-docs/services/lightlevel>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_LIGHT_LEVEL, JD_LIGHT_LEVEL_PACK_FORMATS, role)
    

    @property
    def light_level(self) -> Optional[float]:
        """
        Detect light level, _: /
        """
        return self.register(JD_LIGHT_LEVEL_REG_LIGHT_LEVEL).value()

    @property
    def variant(self) -> Optional[LightLevelVariant]:
        """
        (Optional) The type of physical sensor., 
        """
        return self.register(JD_LIGHT_LEVEL_REG_VARIANT).value()

    
