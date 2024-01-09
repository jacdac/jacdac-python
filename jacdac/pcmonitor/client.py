# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, Tuple


class PCMonitorClient(Client):
    """
    Measures PC monitor.
    Implements a client for the `PC monitor <https://microsoft.github.io/jacdac-docs/services/pcmonitor>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_PCMONITOR, JD_PCMONITOR_PACK_FORMATS, role)


    @property
    def cpu_usage(self) -> Optional[int]:
        """
        CPU usage in percent., _: %
        """
        return self.register(JD_PCMONITOR_REG_CPU_USAGE).value()

    @property
    def cpu_temperature(self) -> Optional[int]:
        """
        CPU temperature in Celsius., _: °C
        """
        return self.register(JD_PCMONITOR_REG_CPU_TEMPERATURE).value()

    @property
    def ram_usage(self) -> Optional[int]:
        """
        RAM usage in percent., _: %
        """
        return self.register(JD_PCMONITOR_REG_RAM_USAGE).value()

    @property
    def gpu_information(self) -> Optional[Tuple[int, int]]:
        """
        GPU info., usage: %,temperature: °C
        """
        return self.register(JD_PCMONITOR_REG_GPU_INFORMATION).value()

    @property
    def network_information(self) -> Optional[Tuple[int, int]]:
        """
        Network transmit/receive speed in Kbytes per second.
        
        A measure of PC monitor., tx: KB,rx: KB
        """
        return self.register(JD_PCMONITOR_REG_NETWORK_INFORMATION).value()

    
