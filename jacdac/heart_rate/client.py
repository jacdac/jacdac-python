# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class HeartRateClient(SensorClient):
    """
    A sensor approximating the heart rate. 
     * 
     * 
     * **Jacdac is NOT suitable for medical devices and should NOT be used in any kind of device to diagnose or treat any medical conditions.**
    Implements a client for the `Heart Rate <https://microsoft.github.io/jacdac-docs/services/heartrate>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_HEART_RATE, JD_HEART_RATE_PACK_FORMATS, role, preferred_interval = 1000)
    

    @property
    def heart_rate(self) -> Optional[float]:
        """
        The estimated heart rate., _: bpm
        """
        self.refresh_reading()
        return self.register(JD_HEART_RATE_REG_HEART_RATE).value()

    @property
    def heart_rate_error(self) -> Optional[float]:
        """
        (Optional) The estimated error on the reported sensor data., _: bpm
        """
        return self.register(JD_HEART_RATE_REG_HEART_RATE_ERROR).value()

    @property
    def variant(self) -> Optional[HeartRateVariant]:
        """
        (Optional) The type of physical sensor, 
        """
        return self.register(JD_HEART_RATE_REG_VARIANT).value()

    
