# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class CharacterScreenClient(Client):
    """
    A screen that displays characters.
    Implements a client for the `Character Screen <https://microsoft.github.io/jacdac-docs/services/characterscreen>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_CHARACTER_SCREEN, JD_CHARACTER_SCREEN_PACK_FORMATS, role)
    

    @property
    def message(self) -> Optional[str]:
        """
        Text to show. Use `\n` to break lines., 
        """
        return self.register(JD_CHARACTER_SCREEN_REG_MESSAGE).value()

    @message.setter
    def message(self, value: str) -> None:
        self.register(JD_CHARACTER_SCREEN_REG_MESSAGE).set_values(value)


    @property
    def brightness(self) -> Optional[float]:
        """
        (Optional) Brightness of the screen. `0` means off., _: /
        """
        return self.register(JD_CHARACTER_SCREEN_REG_BRIGHTNESS).float_value(100)

    @brightness.setter
    def brightness(self, value: float) -> None:
        self.register(JD_CHARACTER_SCREEN_REG_BRIGHTNESS).set_values(value / 100)


    @property
    def variant(self) -> Optional[CharacterScreenVariant]:
        """
        (Optional) Describes the type of character LED screen., 
        """
        return self.register(JD_CHARACTER_SCREEN_REG_VARIANT).value()

    @property
    def text_direction(self) -> Optional[CharacterScreenTextDirection]:
        """
        (Optional) Specifies the RTL or LTR direction of the text., 
        """
        return self.register(JD_CHARACTER_SCREEN_REG_TEXT_DIRECTION).value()

    @text_direction.setter
    def text_direction(self, value: CharacterScreenTextDirection) -> None:
        self.register(JD_CHARACTER_SCREEN_REG_TEXT_DIRECTION).set_values(value)


    @property
    def rows(self) -> Optional[int]:
        """
        Gets the number of rows., _: #
        """
        return self.register(JD_CHARACTER_SCREEN_REG_ROWS).value()

    @property
    def columns(self) -> Optional[int]:
        """
        Gets the number of columns., _: #
        """
        return self.register(JD_CHARACTER_SCREEN_REG_COLUMNS).value()


    def set_line(self, index: int, message: str) -> None:
        """
        Overrides the content of a single line at a 0-based index.
        """
        self.send_cmd_packed(JD_CHARACTER_SCREEN_CMD_SET_LINE, index, message)

    def clear(self, ) -> None:
        """
        Clears all text from the display.
        """
        self.send_cmd_packed(JD_CHARACTER_SCREEN_CMD_CLEAR, )
    
