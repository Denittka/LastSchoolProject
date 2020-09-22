from .. import Device, LAN, Remote


class Modem(Device, LAN, Remote):
    def __init__(self, name):
        super().__init__(name)

    def decide(self):
        pass

