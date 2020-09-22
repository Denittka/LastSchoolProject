from .. import Device, LAN, USB


class Server(Device, LAN, USB):
    def __init__(self, name):
        super.__init__(name)

    def decide(self):
        pass

