class Device:
    def __init__(self, name):
        self.name = name
        self.power = False
        return 0

    def change_name(self, name):
        self.name = name
        return 0

    def power_on(self):
        if self.power == True:
            return 3
        self.power = True
        return 0

    def power_off(self):
        if self.power == False:
            return 4
        self.power = False
        return 0
