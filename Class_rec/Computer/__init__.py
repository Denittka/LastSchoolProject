from .. import *
from ..Device import *

class Computer(Device):
    def __init__(self):
        super().__init__()
        self.local = []
        self.usb = []

    def connect_usb(self, device):
        if not isinstance(device, Phone):
            return 7
        self.usb += [device]
        return 0

