class Remote:
    def __init__(self):
        self.remote = []

    def connect_remote(self, device):
        if device in self.remote:
            return 9
        self.remote += [device]
        return 0

    def disconnect_remote(self, device):
        if device not in self.remote:
            return 10
        del self.remote[self.remote.index(device)]
        return 0
