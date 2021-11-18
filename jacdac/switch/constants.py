"""
Autogenerated constants for Switch service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_SWITCH = const(0x1ad29402)


class SwitchVariant(Enum):
    SLIDE = const(0x1)
    TILT = const(0x2)
    PUSH_BUTTON = const(0x3)
    TACTILE = const(0x4)
    TOGGLE = const(0x5)
    PROXIMITY = const(0x6)
    MAGNETIC = const(0x7)
    FOOT_PEDAL = const(0x8)


JD_SWITCH_REG_ACTIVE = const(JD_REG_READING)
JD_SWITCH_REG_VARIANT = const(JD_REG_VARIANT)
JD_SWITCH_REG_AUTO_OFF_DELAY = const(0x180)
JD_SWITCH_EV_ON = const(JD_EV_ACTIVE)
JD_SWITCH_EV_OFF = const(JD_EV_INACTIVE)
JD_SWITCH_PACK_FORMATS = {
    JD_SWITCH_REG_ACTIVE: "u8",
    JD_SWITCH_REG_VARIANT: "u8",
    JD_SWITCH_REG_AUTO_OFF_DELAY: "u16.16"
}
