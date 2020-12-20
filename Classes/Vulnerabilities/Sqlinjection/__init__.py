class SQLInjection:
    def __init__(self):
        self.devices = ["Server", "Computer", "Laptop"]
        self.name = "SQLInjection"

    def do(self, device, command):
        if type(device) in self.devices:
            device.do(command)
            return 0
        return 15
