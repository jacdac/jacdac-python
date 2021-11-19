# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional, Tuple
from jacdac.events import EventHandlerFn, UnsubscribeFn

class AccelerometerClient(SensorClient):
    """
    A 3-axis accelerometer.
    Implements a client for the `Accelerometer <https://microsoft.github.io/jacdac-docs/services/accelerometer>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_ACCELEROMETER, JD_ACCELEROMETER_PACK_FORMATS, role)
    

    @property
    def forces(self) -> Optional[Tuple[float, float, float]]:
        """
        Indicates the current forces acting on accelerometer., x: g,y: g,z: g
        """
        self.refresh_reading()
        return self.register(JD_ACCELEROMETER_REG_FORCES).value()

    @property
    def forces_error(self) -> Optional[float]:
        """
        (Optional) Error on the reading value., _: g
        """
        return self.register(JD_ACCELEROMETER_REG_FORCES_ERROR).value()

    @property
    def max_force(self) -> Optional[float]:
        """
        (Optional) Configures the range forces detected.
        The value will be "rounded up" to one of `max_forces_supported`., _: g
        """
        return self.register(JD_ACCELEROMETER_REG_MAX_FORCE).value()

    @max_force.setter
    def max_force(self, value: float) -> None:
        self.register(JD_ACCELEROMETER_REG_MAX_FORCE).set_values(value)


    def on_tilt_up(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is tilted in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_TILT_UP, handler)

    def on_tilt_down(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is tilted in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_TILT_DOWN, handler)

    def on_tilt_left(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is tilted in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_TILT_LEFT, handler)

    def on_tilt_right(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is tilted in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_TILT_RIGHT, handler)

    def on_face_up(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is laying flat in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FACE_UP, handler)

    def on_face_down(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when accelerometer is laying flat in the given direction.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FACE_DOWN, handler)

    def on_freefall(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when total force acting on accelerometer is much less than 1g.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FREEFALL, handler)

    def on_shake(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when forces change violently a few times.
        """
        return self.on_event(JD_ACCELEROMETER_EV_SHAKE, handler)

    def on_force_2g(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when force in any direction exceeds given threshold.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FORCE_2G, handler)

    def on_force_3g(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when force in any direction exceeds given threshold.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FORCE_3G, handler)

    def on_force_6g(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when force in any direction exceeds given threshold.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FORCE_6G, handler)

    def on_force_8g(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Emitted when force in any direction exceeds given threshold.
        """
        return self.on_event(JD_ACCELEROMETER_EV_FORCE_8G, handler)

    
