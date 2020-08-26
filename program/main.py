from Class import *


def print_devices():
    print(devices)
    return 0


def check_name(name):
    return True if name in [device.name for device in devices] else False


def create(device, name):
    global devices
    devices += [device(name)]
    return 0


def get_type(device):
    if device == "computer":
        return Computer
    return 5


def split(command):
    command = command.split()
    if command[0] == "exit":
        if len(command) > 1:
            return 1
        global run
        run = False
        return 0
    if command[0] == "new":
        device = get_type(command[1])
        if device == 5:
            return device
        if check_name(command[2]):
            return 6
        return create(device, command[2])
    if command[0] == "print":
        return print_devices()
    return 2


def get_result(result):
    if result == 0:
        return "Success"
    if result == 1:
        return "Unexpected arguments"
    if result == 2:
        return "Command not found"
    if result == 3:
        return "This device has already been powered on"
    if result == 4:
        return "This device has already been powered off"
    if result == 5:
        return "The type of this device has not been found"
    if result == 6:
        return "This name is being used"


def main():
    while run:
        command = input("> ")
        result = split(command)
        print(get_result(result))


if __name__ == "__main__":
    run = True
    devices = []
    try:
        main()
    except Exception as error:
        print(error)
        input()
