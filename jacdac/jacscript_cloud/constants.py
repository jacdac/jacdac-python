# Autogenerated constants for Jacscript Cloud service
from enum import IntEnum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_JACSCRIPT_CLOUD = const(0x14606e9c)


class JacscriptCloudCommandStatus(IntEnum):
    OK = const(0xc8)
    NOT_FOUND = const(0x194)
    BUSY = const(0x1ad)


JD_JACSCRIPT_CLOUD_CMD_UPLOAD = const(0x80)
JD_JACSCRIPT_CLOUD_CMD_GET_TWIN = const(0x81)
JD_JACSCRIPT_CLOUD_CMD_ACK_CLOUD_COMMAND = const(0x83)
JD_JACSCRIPT_CLOUD_REG_CONNECTED = const(0x180)
JD_JACSCRIPT_CLOUD_EV_CLOUD_COMMAND = const(0x81)
JD_JACSCRIPT_CLOUD_EV_TWIN_CHANGE = const(JD_EV_CHANGE)
JD_JACSCRIPT_CLOUD_PACK_FORMATS = {
    JD_JACSCRIPT_CLOUD_CMD_UPLOAD: "z r: f64",
    JD_JACSCRIPT_CLOUD_CMD_GET_TWIN: "s",
    JD_JACSCRIPT_CLOUD_CMD_ACK_CLOUD_COMMAND: "u32 u32 r: f64",
    JD_JACSCRIPT_CLOUD_REG_CONNECTED: "u8",
    JD_JACSCRIPT_CLOUD_EV_CLOUD_COMMAND: "u32 z r: f64"
}