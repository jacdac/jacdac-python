# Autogenerated constants for Sound Spectrum service
from jacdac.constants import *
from jacdac.system.constants import *
JD_SERVICE_CLASS_SOUND_SPECTRUM = const(0x157abc1e)
JD_SOUND_SPECTRUM_REG_FREQUENCY_BINS = const(JD_REG_READING)
JD_SOUND_SPECTRUM_REG_ENABLED = const(JD_REG_INTENSITY)
JD_SOUND_SPECTRUM_REG_FFT_POW2_SIZE = const(0x80)
JD_SOUND_SPECTRUM_REG_MIN_DECIBELS = const(0x81)
JD_SOUND_SPECTRUM_REG_MAX_DECIBELS = const(0x82)
JD_SOUND_SPECTRUM_REG_SMOOTHING_TIME_CONSTANT = const(0x83)
JD_SOUND_SPECTRUM__PACK_FORMATS = {
    JD_SOUND_SPECTRUM_REG_FREQUENCY_BINS: "b",
    JD_SOUND_SPECTRUM_REG_ENABLED: "u8",
    JD_SOUND_SPECTRUM_REG_FFT_POW2_SIZE: "u8",
    JD_SOUND_SPECTRUM_REG_MIN_DECIBELS: "i16",
    JD_SOUND_SPECTRUM_REG_MAX_DECIBELS: "i16",
    JD_SOUND_SPECTRUM_REG_SMOOTHING_TIME_CONSTANT: "u0.8"
}