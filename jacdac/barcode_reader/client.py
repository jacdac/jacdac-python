# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client
from .constants import *
from typing import Optional, cast
from jacdac.events import EventHandlerFn, UnsubscribeFn

class BarcodeReaderClient(Client):
    """
    A device that reads various barcodes, like QR codes. For the web, see [BarcodeDetector](https://developer.mozilla.org/en-US/docs/Web/API/BarcodeDetector).
    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_BARCODE_READER, JD_BARCODE_READER_PACK_FORMATS, role)
    

    @property
    def enabled(self) -> Optional[bool]:
        """
        Turns on or off the detection of barcodes., 
        """
        reg = self.register(JD_BARCODE_READER_REG_ENABLED)
        values = reg.values()
        return cast(Optional[bool], values[0] if values else None)

    @enabled.setter
    def enabled(self, value: bool) -> None:
        reg = self.register(JD_BARCODE_READER_REG_ENABLED)
        reg.set_values(value)


    def on_detect(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Raised when a bar code is detected and decoded. If the reader detects multiple codes, it will issue multiple events.
        In case of numeric barcodes, the `data` field should contain the ASCII (which is the same as UTF8 in that case) representation of the number.
        """
        return self.on_event(JD_BARCODE_READER_EV_DETECT, handler)

    