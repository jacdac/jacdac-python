# Autogenerated constants for Light bulb service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_LIGHT_BULB = const(0x1cab054c)
JD_LIGHT_BULB_REG_BRIGHTNESS = const(JD_REG_INTENSITY)
JD_LIGHT_BULB_REG_DIMMEABLE = const(0x180)
JD_LIGHT_BULB_EV_ON = const(JD_EV_ACTIVE)
JD_LIGHT_BULB_EV_OFF = const(JD_EV_INACTIVE)
JD_LIGHT_BULB_PACK_FORMATS = {
    JD_LIGHT_BULB_REG_BRIGHTNESS: "u0.16",
    JD_LIGHT_BULB_REG_DIMMEABLE: "u8"
}
