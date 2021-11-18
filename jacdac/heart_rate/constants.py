"""
Autogenerated constants for Heart Rate service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_HEART_RATE = const(0x166c6dc4)


class HeartRateVariant(Enum):
    FINGER = const(0x1)
    CHEST = const(0x2)
    WRIST = const(0x3)
    PUMP = const(0x4)
    WEB_CAM = const(0x5)


JD_HEART_RATE_REG_HEART_RATE = const(JD_REG_READING)
JD_HEART_RATE_REG_HEART_RATE_ERROR = const(JD_REG_READING_ERROR)
JD_HEART_RATE_REG_VARIANT = const(JD_REG_VARIANT)
JD_HEART_RATE_PACK_FORMATS = {
    JD_HEART_RATE_REG_HEART_RATE: "u16.16",
    JD_HEART_RATE_REG_HEART_RATE_ERROR: "u16.16",
    JD_HEART_RATE_REG_VARIANT: "u8"
}
