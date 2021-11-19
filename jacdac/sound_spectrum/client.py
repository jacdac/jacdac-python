# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class SoundSpectrumClient(SensorClient):
    """
    A microphone that analyzes the sound specturm
    Implements a client for the `Sound Spectrum <https://microsoft.github.io/jacdac-docs/services/soundspectrum>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_SOUND_SPECTRUM, JD_SOUND_SPECTRUM_PACK_FORMATS, role)
    

    @property
    def frequency_bins(self) -> Optional[bytes]:
        """
        The computed frequency data., 
        """
        return self.register(JD_SOUND_SPECTRUM_REG_FREQUENCY_BINS).value()

    @property
    def enabled(self) -> Optional[bool]:
        """
        Turns on/off the micropohone., 
        """
        return self.register(JD_SOUND_SPECTRUM_REG_ENABLED).bool_value()

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self.register(JD_SOUND_SPECTRUM_REG_ENABLED).set_values(value)


    @property
    def fft_pow2_size(self) -> Optional[int]:
        """
        The power of 2 used as the size of the FFT to be used to determine the frequency domain., 
        """
        return self.register(JD_SOUND_SPECTRUM_REG_FFT_POW2_SIZE).value()

    @fft_pow2_size.setter
    def fft_pow2_size(self, value: int) -> None:
        self.register(JD_SOUND_SPECTRUM_REG_FFT_POW2_SIZE).set_values(value)


    @property
    def min_decibels(self) -> Optional[int]:
        """
        The minimum power value in the scaling range for the FFT analysis data, _: dB
        """
        return self.register(JD_SOUND_SPECTRUM_REG_MIN_DECIBELS).value()

    @min_decibels.setter
    def min_decibels(self, value: int) -> None:
        self.register(JD_SOUND_SPECTRUM_REG_MIN_DECIBELS).set_values(value)


    @property
    def max_decibels(self) -> Optional[int]:
        """
        The maximum power value in the scaling range for the FFT analysis data, _: dB
        """
        return self.register(JD_SOUND_SPECTRUM_REG_MAX_DECIBELS).value()

    @max_decibels.setter
    def max_decibels(self, value: int) -> None:
        self.register(JD_SOUND_SPECTRUM_REG_MAX_DECIBELS).set_values(value)


    @property
    def smoothing_time_constant(self) -> Optional[float]:
        """
        The averaging constant with the last analysis frame. 
        If ``0`` is set, there is no averaging done, whereas a value of ``1`` means "overlap the previous and current buffer quite a lot while computing the value"., _: /
        """
        return self.register(JD_SOUND_SPECTRUM_REG_SMOOTHING_TIME_CONSTANT).float_value(100)

    @smoothing_time_constant.setter
    def smoothing_time_constant(self, value: float) -> None:
        self.register(JD_SOUND_SPECTRUM_REG_SMOOTHING_TIME_CONSTANT).set_values(value / 100)


    
