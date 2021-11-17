# Autogenerated constants for MIDI output service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_MIDI_OUTPUT = const(0x1a848cd7)
JD_MIDI_OUTPUT_REG_ENABLED = const(JD_REG_INTENSITY)
JD_MIDI_OUTPUT_CMD_CLEAR = const(0x80)
JD_MIDI_OUTPUT_CMD_SEND = const(0x81)
JD_MIDI_OUTPUT__PACK_FORMATS = {
    JD_MIDI_OUTPUT_REG_ENABLED: "u8",
    JD_MIDI_OUTPUT_CMD_SEND: "b"
}