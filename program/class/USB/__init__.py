class USB:
    def __init__(self):
        self.usb = []
        self.usb_count = 0

    def usb_set_count(self, count):
        if not isinstance(eval(count), int):
            return 9
        if not int(count) >= 0:
            return 10
        if len(self.usb) < int(count):
            return 12
        self.usb_count = count
        return 0

    def usb_connect(self, device):
        if len(self.usb) == self.usb_count:
            return 11
        if device in self.usb:
            return 7
        self.device += [device]
        return 0

    def usb_disconnect(self, device):
        if device not in self.usb:
            return 8
        del self.device[self.device.index(device)]
        return 0

