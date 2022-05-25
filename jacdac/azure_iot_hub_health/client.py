# Autogenerated file. Do not edit.
from jacdac.bus import Bus, Client, EventHandlerFn, UnsubscribeFn
from .constants import *
from typing import Optional


class AzureIotHubHealthClient(Client):
    """
    Health and diagnostics information about the Azure Iot Hub connection.
    Implements a client for the `Azure IoT Hub Health <https://microsoft.github.io/jacdac-docs/services/azureiothubhealth>`_ service.

    """

    def __init__(self, bus: Bus, role: str) -> None:
        super().__init__(bus, JD_SERVICE_CLASS_AZURE_IOT_HUB_HEALTH, JD_AZURE_IOT_HUB_HEALTH_PACK_FORMATS, role)


    @property
    def hub_name(self) -> Optional[str]:
        """
        (Optional) Something like `my-iot-hub.azure-devices.net` if available., 
        """
        return self.register(JD_AZURE_IOT_HUB_HEALTH_REG_HUB_NAME).value()

    @property
    def hub_device_id(self) -> Optional[str]:
        """
        (Optional) Device identifier in Azure Iot Hub if available., 
        """
        return self.register(JD_AZURE_IOT_HUB_HEALTH_REG_HUB_DEVICE_ID).value()

    @property
    def connection_status(self) -> Optional[AzureIotHubHealthConnectionStatus]:
        """
        Indicates the status of connection. A message beyond the [0..3] range represents an HTTP error code., 
        """
        return self.register(JD_AZURE_IOT_HUB_HEALTH_REG_CONNECTION_STATUS).value()

    def on_connection_status_change(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Raised when the connection status changes
        """
        return self.on_event(JD_AZURE_IOT_HUB_HEALTH_EV_CONNECTION_STATUS_CHANGE, handler)

    def on_message_sent(self, handler: EventHandlerFn) -> UnsubscribeFn:
        """
        Raised when a message has been sent to the hub.
        """
        return self.on_event(JD_AZURE_IOT_HUB_HEALTH_EV_MESSAGE_SENT, handler)

    
