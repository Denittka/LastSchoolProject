class LAN:
    def __init__(self):
        self.local = []
        self.local_count = 0

    def local_connect(self, count):
        if not isinstance(eval(count), int):
            return 10
        if not int(count) >= 0:
            return 10
        if len(self.local) < int(count):
            return 12
        self.local_count = int(count)
        return 0

    def connect_LAN(self, device):
        if len(self.local) == self.local_count:
            return 11
        if device in self.LAN:
            return 11
        self.LAN += [device]
        return 0

    def disconnect_LAN(self, device):
        if device not in self.LAN:
            return 12
        del self.LAN[self.LAN.index(device)]
        return 0

