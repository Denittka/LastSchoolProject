from Class import *


DEVICES = []  # Глобальный список всех устройств.


"""
--------------------------------------------------------------------------------
|                        Functions for other functions.                        |
--------------------------------------------------------------------------------
"""


def check_name(name):  # Функция проверки существования имени.
    return name in [device.name for device in DEVICES]


def print_devices():  # Функция вывода информации обо всех устройствах.
    for device in DEVICES:
        model = "Компьютер" if isinstance(device, Computer) else "Сервер"\
            if isinstance(device, Server) else "Телефон"
        local = ", ".join([local_device.name for local_device in device.local]) \
                if len(device.local) > 0 else "устройство не подключено к локальной сети"
        print(model + ":\nname: " + device.name + ";\nLAN: " + local + ";\n\n")
    return 0


"""
--------------------------------------------------------------------------------
|                          Fucntions creating models.                          |
--------------------------------------------------------------------------------
"""


def create(inp):  # Функция определения устройства, которое надо создать.
    if len(inp) < 3:
        return 4
    if check_name(inp[2]):
        return 3
    if inp[1] == "computer":
        return create_computer(inp)
    if inp[1] == "server":
        return create_server(inp)
    if inp[1] == "phone":
        return create_phone(inp)
    return 2


def create_computer(inp):  # Функция создания компьютера.
    global DEVICES
    new_computer = Computer()
    new_computer.set_name(inp[2])
    DEVICES += [new_computer]
    return 0


def create_server(inp):  # Функция создания сервера.
    global DEVICES
    new_server = Server()
    new_server.set_name(inp[2])
    DEVICES += [new_server]
    return 0


def create_phone(inp):  # Функция создания телефона.
    global DEVICES
    new_phone = Phone()
    new_phone.set_name(inp[2])
    DEVICES += [new_phone]
    return 0


"""
def create_router(inp):  # The function of creating routers.
    global DEVICES
    new_router = Router()
    new_router.set_name(inp[2])
    DEVICES += [router]
    return 0
"""  # TODO after creating Router model.


"""
--------------------------------------------------------------------------------
|                        Functions configuring models.                         |
--------------------------------------------------------------------------------
These functions are able to configure any settings of models in the global
devices' list.
"""


# This function parsing an input to find the model a user want to configure.
def configure(inp):
    if len(inp) < 3:
        return 4
    device = None
    for model in DEVICES:
        if model.name == inp[1]:
            device = model
    if device is None:
        return 5
    if inp[2] == "power":
        return configure_power(inp, device)
    return 1


def configure_name():  # This function changes names of models.
    pass  # TODO


def add_local_device():  # This function connects two devices to each other.
    pass  # TODO


def connect_to_wifi():  # This function connects a phone to a router.
    pass  # TODO


def configure_power(inp, device):
    if inp[3] == "on" or inp[3] == "1":
        return device.power_on()
    if inp[3] == "off" or inp[3] == "0":
        return device.power_off()
    return 1


"""
--------------------------------------------------------------------------------
|                                    Parsers                                   |
--------------------------------------------------------------------------------
"""


def parse(inp):  # Функция определения команды.
    global run
    if len(inp) == 0:
        return 4
    if inp[0] == "new":
        return create(inp)
    if inp[0] == "test":
        pass  # TODO
    if inp[0] == "config":
        pass  # TODO
    if inp[0] == "set":
        pass  # TODO
    if inp[0] == "print":
        return print_devices()
    if inp[0] == "exit":
        run = False
        return 0
    return 1


"""
--------------------------------------------------------------------------------
|                                  Main block                                  |
--------------------------------------------------------------------------------
"""


# Prints information about this program.
file = open("data/intro.txt", "r")
print(file.read())
file.close()
# The starting of this program itself.
run = True
while run:
    inp = input("> ").strip().split()  # Accepting inputs of users.
    result = parse(inp)  # Parsing.
    # Here is the block that prints the results.
    if result == 0:
        print("Команда успешно выполнена.")
    if result == 1:
        print("Команда не найдена.")
    if result == 2:
        print("Заданное устройство не найдено.")
    if result == 3:
        print("Данное имя устройства уже занято.")
    if result == 4:
        print("Введён пустой запрос или недостаточно аргументов.")
    if result == 5:
        print("")
    if result == 6:
        print("")
    if result == 7:
        print("")


"""
--------------------------------------------------------------------------------
|                           The end of this program.                           |
--------------------------------------------------------------------------------
"""

