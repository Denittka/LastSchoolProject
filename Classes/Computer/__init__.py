from ..Device import Device
from ..LAN import LAN
from ..USB import USB


class Computer(Device, LAN, USB):
    def __init__(self):
        super().__init__()

    def send(self):
        pass

    def receive(self):
        pass
