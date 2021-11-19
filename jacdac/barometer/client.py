# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast


class BarometerClient(Client):
    """
    A sensor measuring air pressure of outside environment.
    Implements a client for the `Barometer <https://microsoft.github.io/jacdac-docs/services/barometer>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_BAROMETER, JD_BAROMETER_PACK_FORMATS, role)
    

    @property
    def pressure(self) -> Optional[float]:
        """
        The air pressure., _: hPa
        """
        reg = self.register(JD_BAROMETER_REG_PRESSURE)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    @property
    def pressure_error(self) -> Optional[float]:
        """
        The real pressure is between `pressure - pressure_error` and `pressure + pressure_error`., _: hPa
        """
        reg = self.register(JD_BAROMETER_REG_PRESSURE_ERROR)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    
