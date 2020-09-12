from .. import Device, LAN


class Computer(Device, LAN):
    def __init__(self, name):
        super().__init__(name)

    def decide(self):
        pass

