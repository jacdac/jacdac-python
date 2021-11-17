# Autogenerated constants for Real time clock service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_REAL_TIME_CLOCK = const(0x1a8b1a28)
JD_REAL_TIME_CLOCK_VARIANT_COMPUTER = const(0x1)
JD_REAL_TIME_CLOCK_VARIANT_CRYSTAL = const(0x2)
JD_REAL_TIME_CLOCK_VARIANT_CUCKOO = const(0x3)
JD_REAL_TIME_CLOCK_REG_LOCAL_TIME = const(JD_REG_READING)
JD_REAL_TIME_CLOCK_REG_ERROR = const(0x180)
JD_REAL_TIME_CLOCK_REG_PRECISION = const(0x181)
JD_REAL_TIME_CLOCK_REG_VARIANT = const(JD_REG_VARIANT)
JD_REAL_TIME_CLOCK_CMD_SET_TIME = const(0x80)
JD_REAL_TIME_CLOCK_PACK_FORMATS = {
    JD_REAL_TIME_CLOCK_REG_LOCAL_TIME: "u16 u8 u8 u8 u8 u8 u8",
    JD_REAL_TIME_CLOCK_REG_ERROR: "u16.16",
    JD_REAL_TIME_CLOCK_REG_PRECISION: "u16.16",
    JD_REAL_TIME_CLOCK_REG_VARIANT: "u8",
    JD_REAL_TIME_CLOCK_CMD_SET_TIME: "u16 u8 u8 u8 u8 u8 u8"
}
