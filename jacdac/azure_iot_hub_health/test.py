from jacdac.devtools import create_dev_tools_bus
from .server import AzureIotHubHealthServer
from time import sleep
import asyncio
import tracemalloc


async def main():
    tracemalloc.start()
    bus = create_dev_tools_bus()
    hub_server = AzureIotHubHealthServer(bus)
    while True:
        sleep(1)
        await hub_server.send_message("hello")

if __name__ == '__main__':
    asyncio.run(main())