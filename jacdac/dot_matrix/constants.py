# Autogenerated constants for Dot Matrix service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_DOT_MATRIX = const(0x110d154b)
JD_DOT_MATRIX_VARIANT_LED = const(0x1)
JD_DOT_MATRIX_VARIANT_BRAILLE = const(0x2)
JD_DOT_MATRIX_REG_DOTS = const(JD_REG_VALUE)
JD_DOT_MATRIX_REG_BRIGHTNESS = const(JD_REG_INTENSITY)
JD_DOT_MATRIX_REG_ROWS = const(0x181)
JD_DOT_MATRIX_REG_COLUMNS = const(0x182)
JD_DOT_MATRIX_REG_VARIANT = const(JD_REG_VARIANT)
JD_DOT_MATRIX_PACK_FORMATS = {
    JD_DOT_MATRIX_REG_DOTS: "b",
    JD_DOT_MATRIX_REG_BRIGHTNESS: "u0.8",
    JD_DOT_MATRIX_REG_ROWS: "u16",
    JD_DOT_MATRIX_REG_COLUMNS: "u16",
    JD_DOT_MATRIX_REG_VARIANT: "u8"
}
