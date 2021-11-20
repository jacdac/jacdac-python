from jacdac.devtools import create_dev_tools_bus
from .server import RealTimeClockServer
from time import sleep, localtime

if __name__ == '__main__':
    bus = create_dev_tools_bus()

    clock = RealTimeClockServer(bus)
    while True:
        print(localtime())
        sleep(5)
