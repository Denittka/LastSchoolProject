class Device:
    def __init__(self):
        self.name = None
        self.power = False

    def set_name(self, name):
        self.name = name
        return 0

    def power_off(self):
        if self.power is False:
            return 6
        self.power = False
        return 0

    def power_on(self):
        if self.power is True:
            return 6
        self.power = True
        return 0

