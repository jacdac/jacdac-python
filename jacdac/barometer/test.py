from typing import Any, Type
from jacdac.devtools import create_dev_tools_bus
from .client import BarometerClient
from time import sleep

bus = create_dev_tools_bus()


def up(data: Any):
    print("up")


def down(data: Any):
    print("down")


def hold(data: list[Type[int]]):
    print("hold", data[0])


barometer = BarometerClient(bus, "barometer")
while True:
    print("pressure: ", barometer.pressure, "e:", barometer.pressure_error)
    sleep(0.2)
