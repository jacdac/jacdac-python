# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class MicrophoneClient(Client):
    """
    A single-channel microphone.
    Implements a client for the `Microphone <https://microsoft.github.io/jacdac-docs/services/microphone>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_MICROPHONE, JD_MICROPHONE_PACK_FORMATS, role)


    @property
    def sampling_period(self) -> Optional[int]:
        """
        Get or set microphone sampling period.
        Sampling rate is `1_000_000 / sampling_period Hz`., _: us
        """
        return self.register(JD_MICROPHONE_REG_SAMPLING_PERIOD).value()

    @sampling_period.setter
    def sampling_period(self, value: int) -> None:
        self.register(JD_MICROPHONE_REG_SAMPLING_PERIOD).set_values(value)


    
