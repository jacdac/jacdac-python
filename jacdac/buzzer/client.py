# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class BuzzerClient(Client):
    """
    A simple buzzer.
    Implements a client for the `Buzzer <https://microsoft.github.io/jacdac-docs/services/buzzer>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_BUZZER, JD_BUZZER_PACK_FORMATS, role)
    

    @property
    def volume(self) -> Optional[float]:
        """
        The volume (duty cycle) of the buzzer., _: /
        """
        return self.register(JD_BUZZER_REG_VOLUME).value()

    @volume.setter
    def volume(self, value: float) -> None:
        self.register(JD_BUZZER_REG_VOLUME).set_values(value)



    def play_tone(self, period: int, duty: int, duration: int) -> None:
        """
        Play a PWM tone with given period and duty for given duration.
        The duty is scaled down with `volume` register.
        To play tone at frequency `F` Hz and volume `V` (in `0..1`) you will want
        to send `P = 1000000 / F` and `D = P * V / 2`.
        """
        self.send_cmd_packed(JD_BUZZER_CMD_PLAY_TONE, period, duty, duration)

    def play_note(self, frequency: int, volume: float, duration: int) -> None:
        """
        Play a note at the given frequency and volume.
        """
        # TODO: implement client command
        raise RuntimeError("client command not implemented")
    
