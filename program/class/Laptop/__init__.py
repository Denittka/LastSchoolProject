from .. import Device, Remote, USB, LAN, Bluetooth


class Laptop(Device, Remote, USB, LAN, Bluetooth):
    def __init__(self, name):
        super().__init__(name)

    def decide(self):
        pass

