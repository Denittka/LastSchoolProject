class Bluetooth:
    def __init__(self):
        self.bluetooth = []
        self.bluetooth_count = 0

    def bluetooth_set_count(self, count):
        if not isinstance(eval(count), int):
            return 9
        if not int(count) >= 0:
            return 10
        if len(self.bluetooth) < int(count):
            return 10
        self.bluetooth_cout = int(count)
        return 0

    def bluetooth_connect(self, device):
        if len(self.bluetooth) == self.bluetooth_cout:
            return 11
        if device in self.bluetooth:
            return 7
        self.bluetooth += [device]
        return 0

    def bluetooth_disconnect(self, device):
        if device not in self.bluetooth:
            return 8
        del self.bluetooth[self.bluetooth.index(device)]
        return 0

