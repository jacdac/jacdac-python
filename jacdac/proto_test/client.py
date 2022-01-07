# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client, EventHandlerFn, UnsubscribeFn
from .constants import *
from typing import Optional, Tuple


class ProtoTestClient(Client):
    """
    This is test service to validate the protocol packet transmissions between the browser and a MCU.
     * Use this page if you are porting Jacdac to a new platform.
    Implements a client for the `Protocol Test <https://microsoft.github.io/jacdac-docs/services/prototest>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_PROTO_TEST, JD_PROTO_TEST_PACK_FORMATS, role)


    @property
    def rw_bool(self) -> Optional[bool]:
        """
        A read write bool register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_BOOL).bool_value()

    @rw_bool.setter
    def rw_bool(self, value: bool) -> None:
        self.register(JD_PROTO_TEST_REG_RW_BOOL).set_values(value)


    @property
    def ro_bool(self) -> Optional[bool]:
        """
        A read only bool register. Mirrors rw_bool., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_BOOL).bool_value()

    @property
    def rw_u32(self) -> Optional[int]:
        """
        A read write u32 register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_U32).value()

    @rw_u32.setter
    def rw_u32(self, value: int) -> None:
        self.register(JD_PROTO_TEST_REG_RW_U32).set_values(value)


    @property
    def ro_u32(self) -> Optional[int]:
        """
        A read only u32 register.. Mirrors rw_u32., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_U32).value()

    @property
    def rw_i32(self) -> Optional[int]:
        """
        A read write i32 register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_I32).value()

    @rw_i32.setter
    def rw_i32(self, value: int) -> None:
        self.register(JD_PROTO_TEST_REG_RW_I32).set_values(value)


    @property
    def ro_i32(self) -> Optional[int]:
        """
        A read only i32 register.. Mirrors rw_i32., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_I32).value()

    @property
    def rw_string(self) -> Optional[str]:
        """
        A read write string register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_STRING).value()

    @rw_string.setter
    def rw_string(self, value: str) -> None:
        self.register(JD_PROTO_TEST_REG_RW_STRING).set_values(value)


    @property
    def ro_string(self) -> Optional[str]:
        """
        A read only string register. Mirrors rw_string., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_STRING).value()

    @property
    def rw_bytes(self) -> Optional[bytes]:
        """
        A read write string register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_BYTES).value()

    @rw_bytes.setter
    def rw_bytes(self, value: bytes) -> None:
        self.register(JD_PROTO_TEST_REG_RW_BYTES).set_values(value)


    @property
    def ro_bytes(self) -> Optional[bytes]:
        """
        A read only string register. Mirrors ro_bytes., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_BYTES).value()

    @property
    def rw_i8_u8_u16_i32(self) -> Optional[Tuple[int, int, int, int]]:
        """
        A read write i8, u8, u16, i32 register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_I8_U8_U16_I32).value()

    @rw_i8_u8_u16_i32.setter
    def rw_i8_u8_u16_i32(self, value: Tuple[int, int, int, int]) -> None:
        self.register(JD_PROTO_TEST_REG_RW_I8_U8_U16_I32).set_values(*value)


    @property
    def ro_i8_u8_u16_i32(self) -> Optional[Tuple[int, int, int, int]]:
        """
        A read only i8, u8, u16, i32 register.. Mirrors rw_i8_u8_u16_i32., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_I8_U8_U16_I32).value()

    @property
    def rw_u8_string(self) -> Optional[Tuple[int, str]]:
        """
        A read write u8, string register., 
        """
        return self.register(JD_PROTO_TEST_REG_RW_U8_STRING).value()

    @rw_u8_string.setter
    def rw_u8_string(self, value: Tuple[int, str]) -> None:
        self.register(JD_PROTO_TEST_REG_RW_U8_STRING).set_values(*value)


    @property
    def ro_u8_string(self) -> Optional[Tuple[int, str]]:
        """
        A read only u8, string register.. Mirrors rw_u8_string., 
        """
        return self.register(JD_PROTO_TEST_REG_RO_U8_STRING).value()

    def on_e_bool(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_bool is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_BOOL, handler)

    def on_e_u32(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_u32 is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_U32, handler)

    def on_e_i32(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_i32 is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_I32, handler)

    def on_e_string(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_string is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_STRING, handler)

    def on_e_bytes(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_bytes is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_BYTES, handler)

    def on_e_i8_u8_u16_i32(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_i8_u8_u16_i32 is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_I8_U8_U16_I32, handler)

    def on_e_u8_string(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        An event raised when rw_u8_string is modified
        """
        return self.on_event(JD_PROTO_TEST_EV_E_U8_STRING, handler)


    def c_bool(self, bo: bool) -> None:
        """
        A command to set rw_bool.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_BOOL, bo)

    def c_u32(self, u32: int) -> None:
        """
        A command to set rw_u32.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_U32, u32)

    def c_i32(self, i32: int) -> None:
        """
        A command to set rw_i32.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_I32, i32)

    def c_string(self, str: str) -> None:
        """
        A command to set rw_string.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_STRING, str)

    def c_bytes(self, bytes: bytes) -> None:
        """
        A command to set rw_string.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_BYTES, bytes)

    def c_i8_u8_u16_i32(self, i8: int, u8: int, u16: int, i32: int) -> None:
        """
        A command to set rw_bytes.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_I8_U8_U16_I32, i8, u8, u16, i32)

    def c_u8_string(self, u8: int, str: str) -> None:
        """
        A command to set rw_u8_string.
        """
        self.send_cmd_packed(JD_PROTO_TEST_CMD_C_U8_STRING, u8, str)
    
