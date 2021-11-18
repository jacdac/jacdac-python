"""
Autogenerated constants for Equivalent CO₂ service
"""
from enum import Enum
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_E_CO2 = const(0x169c9dc6)


class ECO2Variant(Enum):
    VOC = const(0x1)
    NDIR = const(0x2)


JD_E_CO2_REG_E_CO2 = const(JD_REG_READING)
JD_E_CO2_REG_E_CO2_ERROR = const(JD_REG_READING_ERROR)
JD_E_CO2_REG_MIN_E_CO2 = const(JD_REG_MIN_READING)
JD_E_CO2_REG_MAX_E_CO2 = const(JD_REG_MAX_READING)
JD_E_CO2_REG_CONDITIONING_PERIOD = const(0x180)
JD_E_CO2_REG_VARIANT = const(JD_REG_VARIANT)
JD_E_CO2_PACK_FORMATS = {
    JD_E_CO2_REG_E_CO2: "u22.10",
    JD_E_CO2_REG_E_CO2_ERROR: "u22.10",
    JD_E_CO2_REG_MIN_E_CO2: "u22.10",
    JD_E_CO2_REG_MAX_E_CO2: "u22.10",
    JD_E_CO2_REG_CONDITIONING_PERIOD: "u32",
    JD_E_CO2_REG_VARIANT: "u8"
}
