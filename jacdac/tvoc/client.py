# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class TvocClient(Client):
    """
    Measures equivalent Total Volatile Organic Compound levels.
    Implements a client for the `Total Volatile organic compound <https://microsoft.github.io/jacdac-docs/services/tvoc>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_TVOC, JD_TVOC_PACK_FORMATS, role)
    

    @property
    def TVOC(self) -> Optional[float]:
        """
        Total volatile organic compound readings in parts per billion., _: ppb
        """
        return self.register(JD_TVOC_REG_TVOC).value()

    @property
    def TVOC_error(self) -> Optional[float]:
        """
        (Optional) Error on the reading data, _: ppb
        """
        return self.register(JD_TVOC_REG_TVOC_ERROR).value()

    @property
    def min_TVOC(self) -> Optional[float]:
        """
        (Optional) Minimum measurable value, _: ppb
        """
        return self.register(JD_TVOC_REG_MIN_TVOC).value()

    @property
    def max_TVOC(self) -> Optional[float]:
        """
        (Optional) Minimum measurable value, _: ppb
        """
        return self.register(JD_TVOC_REG_MAX_TVOC).value()

    @property
    def conditioning_period(self) -> Optional[int]:
        """
        (Optional) Time required to achieve good sensor stability before measuring after long idle period., _: s
        """
        return self.register(JD_TVOC_REG_CONDITIONING_PERIOD).value()

    
