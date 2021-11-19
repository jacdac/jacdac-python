# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class WeightScaleClient(SensorClient):
    """
    A weight measuring sensor.
    Implements a client for the `Weight Scale <https://microsoft.github.io/jacdac-docs/services/weightscale>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_WEIGHT_SCALE, JD_WEIGHT_SCALE_PACK_FORMATS, role)
    

    @property
    def weight(self) -> Optional[float]:
        """
        The reported weight., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_WEIGHT).value()

    @property
    def weight_error(self) -> Optional[float]:
        """
        (Optional) The estimate error on the reported reading., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_WEIGHT_ERROR).value()

    @property
    def zero_offset(self) -> Optional[float]:
        """
        (Optional) Calibrated zero offset error on the scale, i.e. the measured weight when nothing is on the scale.
        You do not need to subtract that from the reading, it has already been done., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_ZERO_OFFSET).value()

    @zero_offset.setter
    def zero_offset(self, value: float) -> None:
        self.register(JD_WEIGHT_SCALE_REG_ZERO_OFFSET).set_values(value)


    @property
    def gain(self) -> Optional[float]:
        """
        (Optional) Calibrated gain on the weight scale error., 
        """
        return self.register(JD_WEIGHT_SCALE_REG_GAIN).value()

    @gain.setter
    def gain(self, value: float) -> None:
        self.register(JD_WEIGHT_SCALE_REG_GAIN).set_values(value)


    @property
    def max_weight(self) -> Optional[float]:
        """
        (Optional) Maximum supported weight on the scale., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_MAX_WEIGHT).value()

    @property
    def min_weight(self) -> Optional[float]:
        """
        (Optional) Minimum recommend weight on the scale., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_MIN_WEIGHT).value()

    @property
    def weight_resolution(self) -> Optional[float]:
        """
        (Optional) Smallest, yet distinguishable change in reading., _: kg
        """
        return self.register(JD_WEIGHT_SCALE_REG_WEIGHT_RESOLUTION).value()

    @property
    def variant(self) -> Optional[WeightScaleVariant]:
        """
        (Optional) The type of physical scale, 
        """
        return self.register(JD_WEIGHT_SCALE_REG_VARIANT).value()


    def calibrate_zero_offset(self, ) -> None:
        """
        Call this command when there is nothing on the scale. If supported, the module should save the calibration data.
        """
        self.send_cmd_packed(JD_WEIGHT_SCALE_CMD_CALIBRATE_ZERO_OFFSET, )

    def calibrate_gain(self, weight: float) -> None:
        """
        Call this command with the weight of the thing on the scale.
        """
        self.send_cmd_packed(JD_WEIGHT_SCALE_CMD_CALIBRATE_GAIN, weight)
    
