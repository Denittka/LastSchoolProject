from ..USB import USB
from ..LAN import LAN
from ..Remote import Remote
from ..Bluetooth import Bluetooth
from ..Device import Device


class Laptop(Device, Bluetooth, Remote, LAN, USB):
    def __init__(self):
        super().__init__()
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None
        self.usb_connected = []
        self.usb_connection_limit = None
        self.remote_connected = []
        self.remote_connection_limit = None
        self.local_connected = []
        self.local_connection_limit = None
