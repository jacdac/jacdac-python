# Autogenerated constants for Speech synthesis service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_SPEECH_SYNTHESIS = const(0x1204d995)
JD_SPEECH_SYNTHESIS_REG_ENABLED = const(JD_REG_INTENSITY)
JD_SPEECH_SYNTHESIS_REG_LANG = const(0x80)
JD_SPEECH_SYNTHESIS_REG_VOLUME = const(0x81)
JD_SPEECH_SYNTHESIS_REG_PITCH = const(0x82)
JD_SPEECH_SYNTHESIS_REG_RATE = const(0x83)
JD_SPEECH_SYNTHESIS_CMD_SPEAK = const(0x80)
JD_SPEECH_SYNTHESIS_CMD_CANCEL = const(0x81)
JD_SPEECH_SYNTHESIS__PACK_FORMATS = {
    JD_SPEECH_SYNTHESIS_REG_ENABLED: "u8",
    JD_SPEECH_SYNTHESIS_REG_LANG: "s",
    JD_SPEECH_SYNTHESIS_REG_VOLUME: "u0.8",
    JD_SPEECH_SYNTHESIS_REG_PITCH: "u16.16",
    JD_SPEECH_SYNTHESIS_REG_RATE: "u16.16",
    JD_SPEECH_SYNTHESIS_CMD_SPEAK: "s"
}