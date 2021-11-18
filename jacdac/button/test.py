from typing import Any, Type
from jacdac.devtools import create_dev_tools_bus
from .client import ButtonClient
from time import sleep

bus = create_dev_tools_bus()


def up(data: Any):
    print("up")


def down(data: Any):
    print("down")


def hold(data: list[Type[int]]):
    print("hold", data[0])


btn1 = ButtonClient(bus, "btn1")
btn1.on_up(up)
btn1.on_down(down)
btn1.on_hold(hold)

while True:
    print("pressed: ", btn1.pressed)
    print("pressure: ", btn1.pressure)
    sleep(1)
