"""
Autogenerated constants for LED service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_LED = const(0x1e3048f8)


class LedVariant(Enum):
    THROUGH_HOLE = const(0x1)
    SMD = const(0x2)
    POWER = const(0x3)
    BEAD = const(0x4)


JD_LED_CMD_ANIMATE = const(0x80)
JD_LED_REG_COLOR = const(0x180)
JD_LED_REG_MAX_POWER = const(JD_REG_MAX_POWER)
JD_LED_REG_LED_COUNT = const(0x183)
JD_LED_REG_WAVE_LENGTH = const(0x181)
JD_LED_REG_LUMINOUS_INTENSITY = const(0x182)
JD_LED_REG_VARIANT = const(JD_REG_VARIANT)
JD_LED_PACK_FORMATS = {
    JD_LED_CMD_ANIMATE: "u8 u8 u8 u8",
    JD_LED_REG_COLOR: "u8 u8 u8",
    JD_LED_REG_MAX_POWER: "u16",
    JD_LED_REG_LED_COUNT: "u16",
    JD_LED_REG_WAVE_LENGTH: "u16",
    JD_LED_REG_LUMINOUS_INTENSITY: "u16",
    JD_LED_REG_VARIANT: "u8"
}
