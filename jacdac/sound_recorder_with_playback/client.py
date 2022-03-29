# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class SoundRecorderWithPlaybackClient(Client):
    """
    A record and replay module. You can record a few seconds of audio and play it back.
    Implements a client for the `Sound Recorder with Playback <https://microsoft.github.io/jacdac-docs/services/soundrecorderwithplayback>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_SOUND_RECORDER_WITH_PLAYBACK, JD_SOUND_RECORDER_WITH_PLAYBACK_PACK_FORMATS, role)


    @property
    def status(self) -> Optional[SoundRecorderWithPlaybackStatus]:
        """
        Indicate the current status, 
        """
        return self.register(JD_SOUND_RECORDER_WITH_PLAYBACK_REG_STATUS).value()

    @property
    def time(self) -> Optional[int]:
        """
        Milliseconds of audio recorded., _: ms
        """
        return self.register(JD_SOUND_RECORDER_WITH_PLAYBACK_REG_TIME).value()

    @property
    def volume(self) -> Optional[float]:
        """
        (Optional) Playback volume control, _: /
        """
        return self.register(JD_SOUND_RECORDER_WITH_PLAYBACK_REG_VOLUME).float_value(100)

    @volume.setter
    def volume(self, value: float) -> None:
        self.register(JD_SOUND_RECORDER_WITH_PLAYBACK_REG_VOLUME).set_values(value / 100)



    def play(self, ) -> None:
        """
        Replay recorded audio.
        """
        self.send_cmd_packed(JD_SOUND_RECORDER_WITH_PLAYBACK_CMD_PLAY, )

    def record(self, duration: int) -> None:
        """
        Record audio for N milliseconds.
        """
        self.send_cmd_packed(JD_SOUND_RECORDER_WITH_PLAYBACK_CMD_RECORD, duration)

    def cancel(self, ) -> None:
        """
        Cancel record, the `time` register will be updated by already cached data.
        """
        self.send_cmd_packed(JD_SOUND_RECORDER_WITH_PLAYBACK_CMD_CANCEL, )
    