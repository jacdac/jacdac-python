# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast


class RotaryEncoderClient(Client):
    """
    An incremental rotary encoder - converts angular motion of a shaft to digital signal.
    Implements a client for the `Rotary encoder <https://microsoft.github.io/jacdac-docs/services/rotaryencoder>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_ROTARY_ENCODER, JD_ROTARY_ENCODER_PACK_FORMATS, role)
    

    @property
    def position(self) -> Optional[int]:
        """
        Upon device reset starts at `0` (regardless of the shaft position).
        Increases by `1` for a clockwise "click", by `-1` for counter-clockwise., _: #
        """
        reg = self.register(JD_ROTARY_ENCODER_REG_POSITION)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    @property
    def clicks_per_turn(self) -> Optional[int]:
        """
        (Optional) This specifies by how much `position` changes when the crank does 360 degree turn. Typically 12 or 24., _: #
        """
        reg = self.register(JD_ROTARY_ENCODER_REG_CLICKS_PER_TURN)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    
