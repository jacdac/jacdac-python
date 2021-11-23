# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional


class RngClient(Client):
    """
    Generates random numbers using entropy sourced from physical processes.
     * 
     * This typically uses a cryptographical pseudo-random number generator (for example [Fortuna](https://en.wikipedia.org/wiki/Fortuna_(PRNG))),
     * which is periodically re-seeded with entropy coming from some hardware source.
    Implements a client for the `Random Number Generator <https://microsoft.github.io/jacdac-docs/services/rng>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_RNG, JD_RNG_PACK_FORMATS, role)


    @property
    def random(self) -> Optional[bytes]:
        """
        A register that returns a 64 bytes random buffer on every request.
        This never blocks for a long time. If you need additional random bytes, keep querying the register., 
        """
        return self.register(JD_RNG_REG_RANDOM).value()

    @property
    def variant(self) -> Optional[RngVariant]:
        """
        (Optional) The type of algorithm/technique used to generate the number.
        `Quantum` refers to dedicated hardware device generating random noise due to quantum effects.
        `ADCNoise` is the noise from quick readings of analog-digital converter, which reads temperature of the MCU or some floating pin.
        `WebCrypto` refers is used in simulators, where the source of randomness comes from an advanced operating system., 
        """
        return self.register(JD_RNG_REG_VARIANT).value()

    
