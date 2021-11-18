# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast
from jacdac.events import EventHandlerFn, UnsubscribeFn

class ReflectedLightClient(Client):
    """
    A sensor that detects light and dark surfaces, commonly used for line following robots.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_REFLECTED_LIGHT, JD_REFLECTED_LIGHT_PACK_FORMATS, role)
    

    @property
    def brightness(self) -> Optional[float]:
        """
        Reports the reflected brightness. It may be a digital value or, for some sensor, analog value., _: /
        """
        reg = self.register(JD_REFLECTED_LIGHT_REG_BRIGHTNESS)
        values = reg.values()
        return cast(Optional[float], values[0] if values else None)

    @property
    def variant(self) -> Optional[ReflectedLightVariant]:
        """
        (Optional) Type of physical sensor used, 
        """
        reg = self.register(JD_REFLECTED_LIGHT_REG_VARIANT)
        values = reg.values()
        return cast(Optional[ReflectedLightVariant], values[0] if values else None)

    def on_dark(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        The sensor detected a transition from light to dark
        """
        return self.on_event(JD_REFLECTED_LIGHT_EV_DARK, handler)

    def on_light(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        The sensor detected a transition from dark to light
        """
        return self.on_event(JD_REFLECTED_LIGHT_EV_LIGHT, handler)

    