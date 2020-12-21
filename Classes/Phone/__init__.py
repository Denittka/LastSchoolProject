from ..USB import USB
from ..Bluetooth import Bluetooth
from ..Remote import Remote
from ..Device import Device
from ..Packet import Packet


class Phone(Device, Remote, Bluetooth, USB):
    def __init__(self):
        super().__init__()
        self.usb_connected = []
        self.usb_connection_limit = None
        self.remote_connected = []
        self.remote_connection_limit = None
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None

    def send(self, to_address, data=None, packet=None):
        if data is not None and packet is None:
            packet = Packet(to_address, self.name, data)
            packet.add_to_trace(self)
        sent = []
        for device in self.remote_connected:
            if device in sent or device in packet.trace:
                continue
            result = device.receive(self.name, packet)
            if result[0] == 16:
                sent = sent + packet.trace.copy()
                continue
            return result
        return [16, packet]
