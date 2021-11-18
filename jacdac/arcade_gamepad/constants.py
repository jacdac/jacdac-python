"""
Autogenerated constants for Arcade Gamepad service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_ARCADE_GAMEPAD = const(0x1deaa06e)


class ArcadeGamepadButton(Enum):
    LEFT = const(0x1)
    UP = const(0x2)
    RIGHT = const(0x3)
    DOWN = const(0x4)
    A = const(0x5)
    B = const(0x6)
    MENU = const(0x7)
    SELECT = const(0x8)
    RESET = const(0x9)
    EXIT = const(0xa)


JD_ARCADE_GAMEPAD_REG_BUTTONS = const(JD_REG_READING)
JD_ARCADE_GAMEPAD_REG_AVAILABLE_BUTTONS = const(0x180)
JD_ARCADE_GAMEPAD_EV_DOWN = const(JD_EV_ACTIVE)
JD_ARCADE_GAMEPAD_EV_UP = const(JD_EV_INACTIVE)
JD_ARCADE_GAMEPAD_PACK_FORMATS = {
    JD_ARCADE_GAMEPAD_REG_BUTTONS: "r: u8 u0.8",
    JD_ARCADE_GAMEPAD_REG_AVAILABLE_BUTTONS: "r: u8",
    JD_ARCADE_GAMEPAD_EV_DOWN: "u8",
    JD_ARCADE_GAMEPAD_EV_UP: "u8"
}
