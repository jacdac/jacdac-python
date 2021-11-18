"""
Autogenerated constants for Verified Telemetry service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_VERIFIED_TELEMETRY = const(0x2194841f)


class VerifiedTelemetryStatus(Enum):
    UNKNOWN = const(0x0)
    WORKING = const(0x1)
    FAULTY = const(0x2)


class VerifiedTelemetryFingerprintType(Enum):
    FALL_CURVE = const(0x1)
    CURRENT_SENSE = const(0x2)
    CUSTOM = const(0x3)


JD_VERIFIED_TELEMETRY_REG_TELEMETRY_STATUS = const(0x180)
JD_VERIFIED_TELEMETRY_REG_TELEMETRY_STATUS_INTERVAL = const(0x80)
JD_VERIFIED_TELEMETRY_REG_FINGERPRINT_TYPE = const(0x181)
JD_VERIFIED_TELEMETRY_REG_FINGERPRINT_TEMPLATE = const(0x182)
JD_VERIFIED_TELEMETRY_CMD_RESET_FINGERPRINT_TEMPLATE = const(0x80)
JD_VERIFIED_TELEMETRY_CMD_RETRAIN_FINGERPRINT_TEMPLATE = const(0x81)
JD_VERIFIED_TELEMETRY_EV_TELEMETRY_STATUS_CHANGE = const(JD_EV_CHANGE)
JD_VERIFIED_TELEMETRY_EV_FINGERPRINT_TEMPLATE_CHANGE = const(0x80)
JD_VERIFIED_TELEMETRY_PACK_FORMATS = {
    JD_VERIFIED_TELEMETRY_REG_TELEMETRY_STATUS: "u8",
    JD_VERIFIED_TELEMETRY_REG_TELEMETRY_STATUS_INTERVAL: "u32",
    JD_VERIFIED_TELEMETRY_REG_FINGERPRINT_TYPE: "u8",
    JD_VERIFIED_TELEMETRY_REG_FINGERPRINT_TEMPLATE: "u16 b",
    JD_VERIFIED_TELEMETRY_EV_TELEMETRY_STATUS_CHANGE: "u8"
}