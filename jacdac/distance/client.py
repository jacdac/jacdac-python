# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast


class DistanceClient(Client):
    """
    A sensor that determines the distance of an object without any physical contact involved.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_DISTANCE, JD_DISTANCE_PACK_FORMATS, role)
    

    @property
    def distance(self) -> Optional[float]:
        """
        Current distance from the object, _: m
        """
        reg = self.register(JD_DISTANCE_REG_DISTANCE)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    @property
    def min_range(self) -> Optional[float]:
        """
        (Optional) Minimum measurable distance, _: m
        """
        reg = self.register(JD_DISTANCE_REG_MIN_RANGE)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    @property
    def max_range(self) -> Optional[float]:
        """
        (Optional) Maximum measurable distance, _: m
        """
        reg = self.register(JD_DISTANCE_REG_MAX_RANGE)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    @property
    def variant(self) -> Optional[DistanceVariant]:
        """
        (Optional) Determines the type of sensor used., 
        """
        reg = self.register(JD_DISTANCE_REG_VARIANT)
        values = reg.values()
        return cast(Optional[DistanceVariant], values[0] if values else None)

    