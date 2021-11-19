# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional
from jacdac.events import EventHandlerFn, UnsubscribeFn

class LightBulbClient(Client):
    """
    A light bulb controller.
    Implements a client for the `Light bulb <https://microsoft.github.io/jacdac-docs/services/lightbulb>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_LIGHT_BULB, JD_LIGHT_BULB_PACK_FORMATS, role)
    

    @property
    def brightness(self) -> Optional[float]:
        """
        Indicates the brightness of the light bulb. Zero means completely off and 0xffff means completely on.
        For non-dimmeable lights, the value should be clamp to 0xffff for any non-zero value., _: /
        """
        return self.register(JD_LIGHT_BULB_REG_BRIGHTNESS).float_value(100)

    @brightness.setter
    def brightness(self, value: float) -> None:
        self.register(JD_LIGHT_BULB_REG_BRIGHTNESS).set_values(value / 100)


    @property
    def dimmeable(self) -> Optional[bool]:
        """
        (Optional) Indicates if the light supports dimming., 
        """
        return self.register(JD_LIGHT_BULB_REG_DIMMEABLE).bool_value()

    def on_on(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when the light brightness is greater than 0.
        """
        return self.on_event(JD_LIGHT_BULB_EV_ON, handler)

    def on_off(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when the light is completely off with brightness to 0.
        """
        return self.on_event(JD_LIGHT_BULB_EV_OFF, handler)

    
