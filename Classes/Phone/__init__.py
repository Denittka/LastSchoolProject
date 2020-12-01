from ..USB import USB
from ..Bluetooth import Bluetooth
from ..Remote import Remote
from ..Device import Device


class Phone(Device, Remote, Bluetooth, USB):
    def __init__(self):
        super().__init__()
        self.usb_connected = []
        self.usb_connection_limit = None
        self.remote_connected = []
        self.remote_connection_limit = None
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None
