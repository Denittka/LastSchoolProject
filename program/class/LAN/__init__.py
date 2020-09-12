class LAN:
    def __init__(self):
        self.LAN = []

    def connect_LAN(self, device):
        if device in self.LAN:
            return 11
        self.LAN += [device]
        return 0

    def disconnect_LAN(self, device):
        if device not in self.LAN:
            return 12
        del self.LAN[self.LAN.index(device)]
        return 0

