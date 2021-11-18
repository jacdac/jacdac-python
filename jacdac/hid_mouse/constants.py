"""
Autogenerated constants for HID Mouse service
"""
from enum import Enum
from jacdac.constants import *
JD_SERVICE_CLASS_HID_MOUSE = const(0x1885dc1c)


class HidMouseButton(Enum):
    LEFT = const(0x1)
    RIGHT = const(0x2)
    MIDDLE = const(0x4)


class HidMouseButtonEvent(Enum):
    UP = const(0x1)
    DOWN = const(0x2)
    CLICK = const(0x3)
    DOUBLE_CLICK = const(0x4)


JD_HID_MOUSE_CMD_SET_BUTTON = const(0x80)
JD_HID_MOUSE_CMD_MOVE = const(0x81)
JD_HID_MOUSE_CMD_WHEEL = const(0x82)
JD_HID_MOUSE_PACK_FORMATS = {
    JD_HID_MOUSE_CMD_SET_BUTTON: "u16 u8",
    JD_HID_MOUSE_CMD_MOVE: "i16 i16 u16",
    JD_HID_MOUSE_CMD_WHEEL: "i16 u16"
}