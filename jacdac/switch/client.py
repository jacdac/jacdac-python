# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast
from jacdac.events import EventHandlerFn, UnsubscribeFn

class SwitchClient(Client):
    """
    A switch, which keeps its position.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_SWITCH, JD_SWITCH_PACK_FORMATS, role)
    

    @property
    def active(self) -> Optional[bool]:
        """
        Indicates whether the switch is currently active (on)., 
        """
        reg = self.register(JD_SWITCH_REG_ACTIVE)
        values = reg.values()
        return cast(Optional[bool], values[0] if values else None)

    @property
    def variant(self) -> Optional[SwitchVariant]:
        """
        (Optional) Describes the type of switch used., 
        """
        reg = self.register(JD_SWITCH_REG_VARIANT)
        values = reg.values()
        return cast(Optional[SwitchVariant], values[0] if values else None)

    @property
    def auto_off_delay(self) -> Optional[float]:
        """
        (Optional) Specifies the delay without activity to automatically turn off after turning on.
        For example, some light switches in staircases have such a capability., _: s
        """
        reg = self.register(JD_SWITCH_REG_AUTO_OFF_DELAY)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    def on_on(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when switch goes from ``off`` to ``on``.
        """
        return self.on_event(JD_SWITCH_EV_ON, handler)

    def on_off(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when switch goes from ``on`` to ``off``.
        """
        return self.on_event(JD_SWITCH_EV_OFF, handler)

    