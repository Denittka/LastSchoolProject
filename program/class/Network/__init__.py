from .. import *


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
        for device in self.devices:
            if isinstance(device, Computer):
                print("Type: Computer")
            if isinstance(device, Phone):
                print("Type: Phone")
            if isinstance(device, Laptop):
                print("Type: Laptop")
            if isinstance(device, Router):
                print("Type: Router")
            if isinstance(device, Modem):
                print("Type: Modem")
            if isinstance(device, Server):
                print("Type: Server")
            print(f"Name: {device.name}")
            if type(device) in [type(Server), type(Modem), type(Router), type(Laptop), type(Computer]:
                print("LAN: \n" + "\n".join([x.name for x in device.local]))
            if type(device) in [type(Phone), type(Laptop)]:
                print("Bluetooth: \n" + "\n".join([x.name for x in device.bluetooth]))
            if type(device) in [type(Router), type(Modem), type(Phone), type(Laptop)]:
                print("Remote: \n" + "\n".join([x.name for x in device.remote]))
            if type(device) in [type(Computer), type(Server), type(Laptop), type(Phone)]:
                print("USB: \n" + "\n".join([x.name for x in device.remote]))


    def get_names(self):
        return [device.name for device in self.devices]

    def check_name(self, name):
        return name in get_names()

