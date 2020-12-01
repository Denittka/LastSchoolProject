from ..Device import Device
from ..Bluetooth import Bluetooth
from ..Remote import Remote


class TV(Device, Bluetooth, Remote):
    def __init__(self):
        super().__init__()
        self.remote_connected = []
        self.remote_connection_limit = None
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None
