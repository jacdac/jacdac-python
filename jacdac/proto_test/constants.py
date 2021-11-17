# Autogenerated constants for Protocol Test service
from jacdac.constants import *
JD_SERVICE_CLASS_PROTO_TEST = const(0x16c7466a)
JD_PROTO_TEST_REG_RW_BOOL = const(0x81)
JD_PROTO_TEST_REG_RO_BOOL = const(0x181)
JD_PROTO_TEST_REG_RW_U32 = const(0x82)
JD_PROTO_TEST_REG_RO_U32 = const(0x182)
JD_PROTO_TEST_REG_RW_I32 = const(0x83)
JD_PROTO_TEST_REG_RO_I32 = const(0x183)
JD_PROTO_TEST_REG_RW_STRING = const(0x84)
JD_PROTO_TEST_REG_RO_STRING = const(0x184)
JD_PROTO_TEST_REG_RW_BYTES = const(0x85)
JD_PROTO_TEST_REG_RO_BYTES = const(0x185)
JD_PROTO_TEST_REG_RW_I8_U8_U16_I32 = const(0x86)
JD_PROTO_TEST_REG_RO_I8_U8_U16_I32 = const(0x186)
JD_PROTO_TEST_REG_RW_U8_STRING = const(0x87)
JD_PROTO_TEST_REG_RO_U8_STRING = const(0x187)
JD_PROTO_TEST_EV_E_BOOL = const(0x81)
JD_PROTO_TEST_EV_E_U32 = const(0x82)
JD_PROTO_TEST_EV_E_I32 = const(0x83)
JD_PROTO_TEST_EV_E_STRING = const(0x84)
JD_PROTO_TEST_EV_E_BYTES = const(0x85)
JD_PROTO_TEST_EV_E_I8_U8_U16_I32 = const(0x86)
JD_PROTO_TEST_EV_E_U8_STRING = const(0x87)
JD_PROTO_TEST_CMD_C_BOOL = const(0x81)
JD_PROTO_TEST_CMD_C_U32 = const(0x82)
JD_PROTO_TEST_CMD_C_I32 = const(0x83)
JD_PROTO_TEST_CMD_C_STRING = const(0x84)
JD_PROTO_TEST_CMD_C_BYTES = const(0x85)
JD_PROTO_TEST_CMD_C_I8_U8_U16_I32 = const(0x86)
JD_PROTO_TEST_CMD_C_U8_STRING = const(0x87)
JD_PROTO_TEST_CMD_C_REPORT_PIPE = const(0x90)
JD_PROTO_TEST__PACK_FORMATS = {
    JD_PROTO_TEST_REG_RW_BOOL: "u8",
    JD_PROTO_TEST_REG_RO_BOOL: "u8",
    JD_PROTO_TEST_REG_RW_U32: "u32",
    JD_PROTO_TEST_REG_RO_U32: "u32",
    JD_PROTO_TEST_REG_RW_I32: "i32",
    JD_PROTO_TEST_REG_RO_I32: "i32",
    JD_PROTO_TEST_REG_RW_STRING: "s",
    JD_PROTO_TEST_REG_RO_STRING: "s",
    JD_PROTO_TEST_REG_RW_BYTES: "b",
    JD_PROTO_TEST_REG_RO_BYTES: "b",
    JD_PROTO_TEST_REG_RW_I8_U8_U16_I32: "i8 u8 u16 i32",
    JD_PROTO_TEST_REG_RO_I8_U8_U16_I32: "i8 u8 u16 i32",
    JD_PROTO_TEST_REG_RW_U8_STRING: "u8 s",
    JD_PROTO_TEST_REG_RO_U8_STRING: "u8 s",
    JD_PROTO_TEST_EV_E_BOOL: "u8",
    JD_PROTO_TEST_EV_E_U32: "u32",
    JD_PROTO_TEST_EV_E_I32: "i32",
    JD_PROTO_TEST_EV_E_STRING: "s",
    JD_PROTO_TEST_EV_E_BYTES: "b",
    JD_PROTO_TEST_EV_E_I8_U8_U16_I32: "i8 u8 u16 i32",
    JD_PROTO_TEST_EV_E_U8_STRING: "u8 s",
    JD_PROTO_TEST_CMD_C_BOOL: "u8",
    JD_PROTO_TEST_CMD_C_U32: "u32",
    JD_PROTO_TEST_CMD_C_I32: "i32",
    JD_PROTO_TEST_CMD_C_STRING: "s",
    JD_PROTO_TEST_CMD_C_BYTES: "b",
    JD_PROTO_TEST_CMD_C_I8_U8_U16_I32: "i8 u8 u16 i32",
    JD_PROTO_TEST_CMD_C_U8_STRING: "u8 s",
    JD_PROTO_TEST_CMD_C_REPORT_PIPE: "b[12]"
}