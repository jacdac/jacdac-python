# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class ThermometerClient(Client):
    """
    A thermometer measuring outside or inside environment.
    Implements a client for the `Thermometer <https://microsoft.github.io/jacdac-docs/services/thermometer>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_THERMOMETER, JD_THERMOMETER_PACK_FORMATS, role)
    

    @property
    def temperature(self) -> Optional[float]:
        """
        The temperature., _: °C
        """
        return self.register(JD_THERMOMETER_REG_TEMPERATURE).value()

    @property
    def min_temperature(self) -> Optional[float]:
        """
        Lowest temperature that can be reported., _: °C
        """
        return self.register(JD_THERMOMETER_REG_MIN_TEMPERATURE).value()

    @property
    def max_temperature(self) -> Optional[float]:
        """
        Highest temperature that can be reported., _: °C
        """
        return self.register(JD_THERMOMETER_REG_MAX_TEMPERATURE).value()

    @property
    def temperature_error(self) -> Optional[float]:
        """
        The real temperature is between `temperature - temperature_error` and `temperature + temperature_error`., _: °C
        """
        return self.register(JD_THERMOMETER_REG_TEMPERATURE_ERROR).value()

    @property
    def variant(self) -> Optional[ThermometerVariant]:
        """
        (Optional) Specifies the type of thermometer., 
        """
        return self.register(JD_THERMOMETER_REG_VARIANT).value()

    
