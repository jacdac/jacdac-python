"""
Autogenerated constants for Reflected light service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_REFLECTED_LIGHT = const(0x126c4cb2)


class ReflectedLightVariant(Enum):
    INFRARED_DIGITAL = const(0x1)
    INFRARED_ANALOG = const(0x2)


JD_REFLECTED_LIGHT_REG_BRIGHTNESS = const(JD_REG_READING)
JD_REFLECTED_LIGHT_REG_VARIANT = const(JD_REG_VARIANT)
JD_REFLECTED_LIGHT_EV_DARK = const(JD_EV_INACTIVE)
JD_REFLECTED_LIGHT_EV_LIGHT = const(JD_EV_ACTIVE)
JD_REFLECTED_LIGHT_PACK_FORMATS = {
    JD_REFLECTED_LIGHT_REG_BRIGHTNESS: "u0.16",
    JD_REFLECTED_LIGHT_REG_VARIANT: "u8"
}
