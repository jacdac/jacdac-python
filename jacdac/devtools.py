from jacdac.logger.constants import JD_LOGGER_PRIORITY_DEBUG
from .bus import Bus
from .transports.ws import WebSocketTransport


def create_dev_tools_bus(*, device_description: str = None):
    """Starts a Jacdac bus connected to the local detools websocket server
    at ws://localhost:8081 .

    Returns:
        Bus: Jacdac bus using local websocket
    """
    print("jacdac-python dev tools")
    print("run scripts/devtools.sh to launch the development server")
    print("open http://localhost:8081 to connect")
    transport = WebSocketTransport("ws://localhost:8081")
    bus = Bus(transport,
              device_description=device_description,
              default_logger_min_priority=JD_LOGGER_PRIORITY_DEBUG
              )
    return bus


if __name__ == "__main__":
    create_dev_tools_bus()
