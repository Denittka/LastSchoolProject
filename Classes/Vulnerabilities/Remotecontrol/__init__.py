class RemoteControl:
    def __init__(self):
        self.devices = ["Server", "Computer", "Laptop"]
        self.allowed = []
        self.name = "RemoteControl"

    def add_device(self, device):
        if device in self.allowed:
            return 5
        self.allowed += [device]
        return 0

    def del_device(self, device):
        if device not in self.allowed:
            return 4
        del self.allowed[self.allowed.index(device)]
        return 0
