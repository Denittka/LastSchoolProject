from ...TV import TV
from ...Computer import Computer
from ...Server import Server
from ...Phone import Phone
from ...Laptop import Laptop
from ...Router import Router


class CriticalError:
    def __init__(self):
        self.devices = [TV, Computer, Server, Phone, Laptop, Router]
        self.name = "CriticalError"

    def do(self, device):
        if type(device) in self.devices:
            device.shut_down()
            return 0
        return 15
