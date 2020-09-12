class Bluetooth:
    def __init__(self):
        self.bluetooth = []

    def connect_bluetooth(self, device):
        if device in self.bluetooth:
            return 7
        self.bluetooth += [device]
        return 0

    def disconnect_bluetooth(self, device):
        if device not in self.bluetooth:
            return 8
        del self.bluetooth[self.bluetooth.index(device)]
        return 0

