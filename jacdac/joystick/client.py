# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional
from jacdac.events import EventHandlerFn, UnsubscribeFn

class JoystickClient(SensorClient):
    """
    A two axis directional joystick
    Implements a client for the `Joystick <https://microsoft.github.io/jacdac-docs/services/joystick>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_JOYSTICK, JD_JOYSTICK_PACK_FORMATS, role)
    

    @property
    def direction(self) -> Optional[tuple[JoystickButtons, float, float]]:
        """
        If the joystick is analog, the directional buttons should be "simulated", based on joystick position
        (`Left` is `{ x = -1, y = 0 }`, `Up` is `{ x = 0, y = -1}`).
        If the joystick is digital, then each direction will read as either `-1`, `0`, or `1` (in fixed representation).
        The primary button on the joystick is `A`., x: /,y: /
        """
        return self.register(JD_JOYSTICK_REG_DIRECTION).value()

    @property
    def variant(self) -> Optional[JoystickVariant]:
        """
        (Optional) The type of physical joystick., 
        """
        return self.register(JD_JOYSTICK_REG_VARIANT).value()

    @property
    def buttons_available(self) -> Optional[JoystickButtons]:
        """
        Indicates a bitmask of the buttons that are mounted on the joystick.
        If the `Left`/`Up`/`Right`/`Down` buttons are marked as available here, the joystick is digital.
        Even when marked as not available, they will still be simulated based on the analog joystick., 
        """
        return self.register(JD_JOYSTICK_REG_BUTTONS_AVAILABLE).value()

    def on_buttons_changed(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted whenever the state of buttons changes.
        """
        return self.on_event(JD_JOYSTICK_EV_BUTTONS_CHANGED, handler)

    
