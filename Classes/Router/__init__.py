from ..Remote import Remote
from ..Device import Device
from ..LAN import LAN


class Router(Device, LAN, Remote):
    def __init__(self):
        super().__init__()
        self.remote_connected = []
        self.remote_connection_limit = None
        self.local_connected = []
        self.local_connection_limit = None
