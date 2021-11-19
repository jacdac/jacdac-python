# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class LedPixelClient(Client):
    """
    A controller for strips of individually controlled RGB LEDs.
    Implements a client for the `LED Pixel <https://microsoft.github.io/jacdac-docs/services/ledpixel>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_LED_PIXEL, JD_LED_PIXEL_PACK_FORMATS, role)
    

    @property
    def brightness(self) -> Optional[float]:
        """
        Set the luminosity of the strip.
        At `0` the power to the strip is completely shut down., _: /
        """
        return self.register(JD_LED_PIXEL_REG_BRIGHTNESS).value()

    @brightness.setter
    def brightness(self, value: float) -> None:
        self.register(JD_LED_PIXEL_REG_BRIGHTNESS).set_values(value)


    @property
    def actual_brightness(self) -> Optional[float]:
        """
        This is the luminosity actually applied to the strip.
        May be lower than `brightness` if power-limited by the `max_power` register.
        It will rise slowly (few seconds) back to `brightness` is limits are no longer required., _: /
        """
        return self.register(JD_LED_PIXEL_REG_ACTUAL_BRIGHTNESS).value()

    @property
    def light_type(self) -> Optional[LedPixelLightType]:
        """
        Specifies the type of light strip connected to controller.
        Controllers which are sold with lights should default to the correct type
        and could not allow change., 
        """
        return self.register(JD_LED_PIXEL_REG_LIGHT_TYPE).value()

    @light_type.setter
    def light_type(self, value: LedPixelLightType) -> None:
        self.register(JD_LED_PIXEL_REG_LIGHT_TYPE).set_values(value)


    @property
    def num_pixels(self) -> Optional[int]:
        """
        Specifies the number of pixels in the strip.
        Controllers which are sold with lights should default to the correct length
        and could not allow change. Increasing length at runtime leads to ineffective use of memory and may lead to controller reboot., _: #
        """
        return self.register(JD_LED_PIXEL_REG_NUM_PIXELS).value()

    @num_pixels.setter
    def num_pixels(self, value: int) -> None:
        self.register(JD_LED_PIXEL_REG_NUM_PIXELS).set_values(value)


    @property
    def num_columns(self) -> Optional[int]:
        """
        (Optional) If the LED pixel strip is a matrix, specifies the number of columns. Otherwise, a square shape is assumed. Controllers which are sold with lights should default to the correct length
        and could not allow change. Increasing length at runtime leads to ineffective use of memory and may lead to controller reboot., _: #
        """
        return self.register(JD_LED_PIXEL_REG_NUM_COLUMNS).value()

    @num_columns.setter
    def num_columns(self, value: int) -> None:
        self.register(JD_LED_PIXEL_REG_NUM_COLUMNS).set_values(value)


    @property
    def max_power(self) -> Optional[int]:
        """
        Limit the power drawn by the light-strip (and controller)., _: mA
        """
        return self.register(JD_LED_PIXEL_REG_MAX_POWER).value()

    @max_power.setter
    def max_power(self, value: int) -> None:
        self.register(JD_LED_PIXEL_REG_MAX_POWER).set_values(value)


    @property
    def max_pixels(self) -> Optional[int]:
        """
        The maximum supported number of pixels.
        All writes to `num_pixels` are clamped to `max_pixels`., _: #
        """
        return self.register(JD_LED_PIXEL_REG_MAX_PIXELS).value()

    @property
    def num_repeats(self) -> Optional[int]:
        """
        How many times to repeat the program passed in `run` command.
        Should be set before the `run` command.
        Setting to `0` means to repeat forever., _: #
        """
        return self.register(JD_LED_PIXEL_REG_NUM_REPEATS).value()

    @num_repeats.setter
    def num_repeats(self, value: int) -> None:
        self.register(JD_LED_PIXEL_REG_NUM_REPEATS).set_values(value)


    @property
    def variant(self) -> Optional[LedPixelVariant]:
        """
        (Optional) Specifies the shape of the light strip., 
        """
        return self.register(JD_LED_PIXEL_REG_VARIANT).value()


    def run(self, program: bytes) -> None:
        """
        Run the given light "program". See service description for details.
        """
        self.send_cmd_packed(JD_LED_PIXEL_CMD_RUN, program)
    
