# Autogenerated file. Do not edit.
from jacdac.bus import Bus, SensorClient
from .constants import *
from typing import Optional


class UvIndexClient(SensorClient):
    """
    The UV Index is a measure of the intensity of ultraviolet (UV) rays from the Sun.
    Implements a client for the `UV index <https://microsoft.github.io/jacdac-docs/services/uvindex>`_ service.
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_UV_INDEX, JD_UV_INDEX_PACK_FORMATS, role)
    

    @property
    def uv_index(self) -> Optional[float]:
        """
        Ultraviolet index, typically refreshed every second., _: uv
        """
        return self.register(JD_UV_INDEX_REG_UV_INDEX).value()

    @property
    def uv_index_error(self) -> Optional[float]:
        """
        (Optional) Error on the UV measure., _: uv
        """
        return self.register(JD_UV_INDEX_REG_UV_INDEX_ERROR).value()

    @property
    def variant(self) -> Optional[UvIndexVariant]:
        """
        (Optional) The type of physical sensor and capabilities., 
        """
        return self.register(JD_UV_INDEX_REG_VARIANT).value()

    
