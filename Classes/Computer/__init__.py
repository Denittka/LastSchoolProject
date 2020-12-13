from ..Device import Device
from ..LAN import LAN
from ..USB import USB
from ..Packet import Packet


class Computer(Device, LAN, USB):
    def __init__(self):
        super().__init__()
        self.usb_connected = []
        self.usb_connection_limit = None
        self.local_connected = []
        self.local_connection_limit = None

    def send(self, to_address, data):
        packet = Packet(to_address, self.name, data)
        for device in self.usb_connected:
            device.receive(self.name, packet)

    def receive(self, from_address, packet):
        if packet.to_address == self.name:
            return self.do(packet.data)
        packet.last_address = self.name
        to_send = []
        for device in to_send:
            device.receive(self.name, packet)
