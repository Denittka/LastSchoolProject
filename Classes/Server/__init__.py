from ..USB import USB
from ..LAN import LAN
from ..Device import Device


class Server(Device, USB, LAN):
    def __init__(self):
        super().__init__()
        self.usb_connected = []
        self.usb_connection_limit = None
        self.local_connected = []
        self.local_connection_limit = None
