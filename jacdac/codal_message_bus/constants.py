# Autogenerated constants for CODAL Message Bus service
from jacdac.constants import *
JD_SERVICE_CLASS_CODAL_MESSAGE_BUS = const(0x121ff81d)
JD_CODAL_MESSAGE_BUS_CMD_SEND = const(0x80)
JD_CODAL_MESSAGE_BUS_EV_MESSAGE = const(0x80)
JD_CODAL_MESSAGE_BUS_PACK_FORMATS = {
    JD_CODAL_MESSAGE_BUS_CMD_SEND: "u16 u16",
    JD_CODAL_MESSAGE_BUS_EV_MESSAGE: "u16 u16"
}
