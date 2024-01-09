# Autogenerated constants for PC controller service
from jacdac.constants import *
JD_SERVICE_CLASS_PCCONTROLLER = const(0x113d0987)
JD_PCCONTROLLER_CMD_OPEN_URL = const(0x80)
JD_PCCONTROLLER_CMD_START_APP = const(0x81)
JD_PCCONTROLLER_CMD_SEND_TEXT = const(0x82)
JD_PCCONTROLLER_CMD_RUN_SCRIPT = const(0x83)
JD_PCCONTROLLER_PACK_FORMATS = {
    JD_PCCONTROLLER_CMD_OPEN_URL: "s",
    JD_PCCONTROLLER_CMD_START_APP: "s",
    JD_PCCONTROLLER_CMD_SEND_TEXT: "s",
    JD_PCCONTROLLER_CMD_RUN_SCRIPT: "s"
}
