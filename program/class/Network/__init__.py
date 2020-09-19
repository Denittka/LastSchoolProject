class Network:
    def __init__(self):
        self.devices = []

    def get_device(self, name):
        return self.devices[get_names().index(name)]

    def add_device(self, device):
        if self.check_name(device):
            return 6
        self.devices += [device]
        return 0

    def delete_device(self, name):
        if not self.check_name(name):
            return 13
        del self.devices[get_device(name)]
        return 0

    def get_list(self):
        return self.devices  # TODO

    def get_names(self):
        return [device.name for device in self.devices]

    def check_name(self, name):
        return name in get_names()

