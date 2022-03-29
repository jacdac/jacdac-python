# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class DcCurrentMeasurementClient(SensorClient):
    """
    A service that reports a current measurement.
    Implements a client for the `DC Current Measurement <https://microsoft.github.io/jacdac-docs/services/dccurrentmeasurement>`_ service.

    """

    def __init__(self, bus: Bus, role: str, *, missing_measurement_value: float = None) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_DC_CURRENT_MEASUREMENT, JD_DC_CURRENT_MEASUREMENT_PACK_FORMATS, role)
        self.missing_measurement_value = missing_measurement_value

    @property
    def measurement_name(self) -> Optional[str]:
        """
        A string containing the net name that is being measured e.g. `POWER_DUT` or a reference e.g. `DIFF_DEV1_DEV2`. These constants can be used to identify a measurement from client code., 
        """
        return self.register(JD_DC_CURRENT_MEASUREMENT_REG_MEASUREMENT_NAME).value()

    @property
    def measurement(self) -> Optional[float]:
        """
        The current measurement., _: A
        """
        self.refresh_reading()
        return self.register(JD_DC_CURRENT_MEASUREMENT_REG_MEASUREMENT).value(self.missing_measurement_value)

    