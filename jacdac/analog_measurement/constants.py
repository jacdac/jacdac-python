# Autogenerated constants for Analog Measurement service
from enum import IntEnum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_ANALOG_MEASUREMENT = const(0x1633ac19)


class AnalogMeasurementADCMeasurementType(IntEnum):
    ABSOLUTE = const(0x0)
    DIFFERENTIAL = const(0x1)


JD_ANALOG_MEASUREMENT_REG_MEASUREMENT_TYPE = const(0x181)
JD_ANALOG_MEASUREMENT_REG_MEASUREMENT_NAME = const(0x182)
JD_ANALOG_MEASUREMENT_REG_MEASUREMENT = const(JD_REG_READING)
JD_ANALOG_MEASUREMENT_PACK_FORMATS = {
    JD_ANALOG_MEASUREMENT_REG_MEASUREMENT_TYPE: "u8",
    JD_ANALOG_MEASUREMENT_REG_MEASUREMENT_NAME: "s",
    JD_ANALOG_MEASUREMENT_REG_MEASUREMENT: "f64"
}
