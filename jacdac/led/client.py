# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast


class LedClient(Client):
    """
    A controller for 1 or more monochrome or RGB LEDs connected in parallel.
    Implements a client for the `LED <https://microsoft.github.io/jacdac-docs/services/led>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_LED, JD_LED_PACK_FORMATS, role)
    

    @property
    def color(self) -> Optional[tuple[int, int, int]]:
        """
        The current color of the LED., 
        """
        reg = self.register(JD_LED_REG_COLOR)
        values = reg.values()
        return cast(Optional[tuple[int, int, int]], values)

    @property
    def max_power(self) -> Optional[int]:
        """
        (Optional) Limit the power drawn by the light-strip (and controller)., _: mA
        """
        reg = self.register(JD_LED_REG_MAX_POWER)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    @max_power.setter
    def max_power(self, value: int) -> None:
        reg = self.register(JD_LED_REG_MAX_POWER)
        reg.set_values(value)


    @property
    def led_count(self) -> Optional[int]:
        """
        (Optional) If known, specifies the number of LEDs in parallel on this device., 
        """
        reg = self.register(JD_LED_REG_LED_COUNT)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    @property
    def wave_length(self) -> Optional[int]:
        """
        (Optional) If monochrome LED, specifies the wave length of the LED., _: nm
        """
        reg = self.register(JD_LED_REG_WAVE_LENGTH)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    @property
    def luminous_intensity(self) -> Optional[int]:
        """
        (Optional) The luminous intensity of the LED, at full value, in micro candella., _: mcd
        """
        reg = self.register(JD_LED_REG_LUMINOUS_INTENSITY)
        values = reg.values()
        return cast(Optional[int], values[0] if values else None)

    @property
    def variant(self) -> Optional[LedVariant]:
        """
        (Optional) The physical type of LED., 
        """
        reg = self.register(JD_LED_REG_VARIANT)
        values = reg.values()
        return cast(Optional[LedVariant], values[0] if values else None)


    def animate(self, to_red: int, to_green: int, to_blue: int, speed: int) -> None:
        """
        This has the same semantics as `set_status_light` in the control service.
        """
        self.send_cmd_packed(JD_LED_CMD_ANIMATE, to_red, to_green, to_blue, speed)
    
