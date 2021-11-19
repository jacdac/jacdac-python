# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class ColorClient(SensorClient):
    """
    Senses RGB colors
    Implements a client for the `Color <https://microsoft.github.io/jacdac-docs/services/color>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_COLOR, JD_COLOR_PACK_FORMATS, role)
    

    @property
    def color(self) -> Optional[tuple[float, float, float]]:
        """
        Detected color in the RGB color space., red: /,green: /,blue: /
        """
        self.refresh_reading()
        return self.register(JD_COLOR_REG_COLOR).value()

    
