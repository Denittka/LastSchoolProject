import os
from Classes.Computer import Computer
from Classes.Laptop import Laptop
from Classes.Phone import Phone
from Classes.Router import Router
from Classes.Server import Server
from Classes.TV import TV
import sqlite3


def init_table(table_name):
    global NAME
    NAME = table_name
    with sqlite3.connect("db.sqlite") as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name};")
        devices = cur.fetchall()
    global environment
    for device in devices:
        new_device = None
        if device[1] == "computer":
            new_device = Computer()
        if device[1] == "laptop":
            new_device = Laptop()
        if device[1] == "phone":
            new_device = Phone()
        if device[1] == "router":
            new_device = Router()
        if device[1] == "server":
            new_device = Server()
        if device[1] == "tv":
            new_device = TV()
        new_device.name = device[2]
        if type(new_device) in [Computer, Server, Phone, Laptop]:
            new_device.usb_connected = device[5].split(", ")
            if new_device.usb_connected[0] == "":
                new_device.usb_connected = []
            if device[10] != "":
                new_device.usb_connection_limit = int(device[10])
        if type(new_device) in [Computer, Router, Server, Laptop]:
            new_device.local_connected = device[3].split(", ")
            if new_device.local_connected[0] == "":
                new_device.local_connected = []
            if device[8] != "":
                new_device.local_connection_limit = int(device[8])
        if type(new_device) in [Router, Laptop, Phone, TV]:
            new_device.remote_connected = device[4].split(", ")
            if new_device.remote_connected[0] == "":
                new_device.remote_connected = []
            if device[9] != "":
                new_device.remote_connection_limit = int(device[9])
        if type(new_device) in [Laptop, Phone, TV]:
            new_device.bluetooth_connected = device[6].split(", ")
            if new_device.bluetooth_connected[0] == "":
                new_device.bluetooth_connected = []
            if device[11] != "":
                new_device.bluetooth_connection_limit = int(device[11])
        new_device_vulnerabilities = device[7].split(", ")
        if new_device_vulnerabilities[0].strip() == "":
            new_device_vulnerabilities = []
        for vulnerability in new_device_vulnerabilities:
            new_device.set_vulnerability(vulnerability.lower())
        environment += [new_device]
    for device in environment:
        if type(device) in [Computer, Server, Phone, Laptop]:
            device.usb_connected = [get_device(name) for name in device.usb_connected]
        if type(device) in [Computer, Router, Server, Laptop]:
            device.local_connected = [get_device(name) for name in device.local_connected]
        if type(device) in [Router, Laptop, Phone, TV]:
            device.remote_connected = [get_device(name) for name in device.remote_connected]
        if type(device) in [Laptop, Phone, TV]:
            device.bluetooth_connected = [get_device(name) for name in device.bluetooth_connected]


def exit_program():
    with sqlite3.connect("db.sqlite") as conn:
        cur = conn.cursor()
        cur.execute(F"DELETE FROM {NAME}")
        for device in environment:
            device_usb_limit, device_lan_limit, device_remote_limit, device_bluetooth_limit = "", "", "", ""
            if isinstance(device, Computer):
                device_type = "computer"
            elif isinstance(device, Laptop):
                device_type = "laptop"
            elif isinstance(device, Phone):
                device_type = "phone"
            elif isinstance(device, Router):
                device_type = "router"
            elif isinstance(device, Server):
                device_type = "server"
            elif isinstance(device, TV):
                device_type = "tv"
            else:
                return 11
            if type(device) in [Computer, Laptop, Phone, Server]:
                device_usb = ", ".join([conn_device.name for conn_device in device.usb_connected])
                if device.usb_connection_limit is not None:
                    device_usb_limit = device.usb_connection_limit
            else:
                device_usb = ""
            if type(device) in [Computer, Laptop, Server, Router]:
                device_lan = ", ".join([conn_device.name for conn_device in device.local_connected])
                if device.local_connection_limit is not None:
                    device_lan_limit = device.local_connection_limit
            else:
                device_lan = ""
            if type(device) in [Laptop, Router, Phone, TV]:
                device_remote = ", ".join([conn_device.name for conn_device in device.remote_connected])
                if device.remote_connection_limit is not None:
                    device_remote_limit = device.remote_connection_limit
            else:
                device_remote = ""
            if type(device) in [Phone, Laptop, TV]:
                device_bluetooth = ", ".join([conn_device.name for conn_device in device.bluetooth_connected])
                if device.bluetooth_connection_limit is not None:
                    device_bluetooth_limit = device.bluetooth_connection_limit
            else:
                device_bluetooth = ""
            device_vulnerabilities = ", ".join([vulnerability.name for vulnerability in device.vulnerabilities])
            sql = """INSERT INTO {}(device, name, usb, lan, remote, bluetooth, vulnerabilities, usb_limit, lan_limit,
            remote_limit, bluetooth_limit)
            VALUES(\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\");""".format(
                NAME, device_type, device.name, device_usb, device_lan, device_remote, device_bluetooth,
                device_vulnerabilities, device_usb_limit, device_lan_limit, device_remote_limit, device_bluetooth_limit)
            cur.execute(sql)


def check_name(name):
    if name in [device.name for device in environment]:
        return True
    return False


def delete(name):
    if check_name(name):
        del environment[[device.name for device in environment].index(name)]
        return 0
    return 12


def create(new_device):
    if len(new_device) < 2:
        return 10
    if check_name(new_device[1]):
        return 9
    if new_device[0] == "computer":
        add_device = Computer()
    elif new_device[0] == "router":
        add_device = Router()
    elif new_device[0] == "server":
        add_device = Server()
    elif new_device[0] == "tv":
        add_device = TV()
    elif new_device[0] == "phone":
        add_device = Phone()
    elif new_device[0] == "laptop":
        add_device = Laptop()
    else:
        return 11
    add_device.set_name(new_device[1])
    global environment
    environment += [add_device]
    return 0


def create_record():
    while True:
        name = input("Введите название записи: ").strip()
        if name == "exit":
            choose_option()
            break
        global NAME
        NAME = name
        print("Создание новой базы данных...")
        with sqlite3.connect("db.sqlite") as conn:
            cur = conn.cursor()
            try:
                cur.execute(f"""CREATE TABLE {NAME} (\
                ID INTEGER, device VARCHAR, name VARCHAR, LAN VARCHAR, Remote VARCHAR, USB VARCHAR, Bluetooth VARCHAR,\
                vulnerabilities VARCHAR, LAN_limit INTEGER, Remote_limit INTEGER, USB_limit INTEGER,\
                Bluetooth_limit INTEGER, PRIMARY KEY(ID));""")
                break
            except sqlite3.OperationalError:
                print("Что-то пошло не так. Видимо, такое имя записи уже занято.")
    print("Запись создана.")


def open_record():
    with sqlite3.connect("db.sqlite") as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM sqlite_master WHERE TYPE=\'table\';")
        tables = cur.fetchall()
    for num, table in enumerate(tables):
        print(f"{num + 1}. {table[1]}")
    while num := input("Какую запись открыть?: "):
        if num == "exit":
            choose_option()
            break
        try:
            num = int(num)
        except ValueError:
            print("Неверно введённое событие.")
            continue
        if -1 < num - 1 < len(tables):
            print(f"Инициализируется запись {tables[num - 1][1]}...")
            init_table(tables[num - 1][1])
            print("Инициализация успешно завершена.")
            break
        else:
            print("Записи с таким номером не существует.")


def print_limits():
    for device in environment:
        if isinstance(device, Computer):
            device_type = "computer"
        elif isinstance(device, Laptop):
            device_type = "laptop"
        elif isinstance(device, Phone):
            device_type = "phone"
        elif isinstance(device, Router):
            device_type = "router"
        elif isinstance(device, Server):
            device_type = "server"
        elif isinstance(device, TV):
            device_type = "tv"
        else:
            return 11
        if type(device) in [Computer, Laptop, Phone, Server] and device.usb_connection_limit is not None:
            device_usb = device.usb_connection_limit
        else:
            device_usb = ""
        if type(device) in [Computer, Laptop, Server, Router] and device.local_connection_limit is not None:
            device_lan = device.local_connection_limit
        else:
            device_lan = ""
        if type(device) in [Laptop, Router, Phone, TV] and device.remote_connection_limit is not None:
            device_remote = device.remote_connection_limit
        else:
            device_remote = ""
        if type(device) in [Phone, Laptop, TV] and device.bluetooth_connection_limit is not None:
            device_bluetooth = device.bluetooth_connection_limit
        else:
            device_bluetooth = ""
        print("------------------------------------")
        print(f"Type: {device_type}")
        print(f"Name: {device.name}")
        print(f"USB limit: {device_usb}")
        print(f"LAN limit: {device_lan}")
        print(f"Remote limit: {device_remote}")
        print(f"Bluetooth limit: {device_bluetooth}")
        print("------------------------------------")


def print_devices():
    for device in environment:
        if isinstance(device, Computer):
            device_type = "computer"
        elif isinstance(device, Laptop):
            device_type = "laptop"
        elif isinstance(device, Phone):
            device_type = "phone"
        elif isinstance(device, Router):
            device_type = "router"
        elif isinstance(device, Server):
            device_type = "server"
        elif isinstance(device, TV):
            device_type = "tv"
        else:
            return 11
        if type(device) in [Computer, Laptop, Phone, Server]:
            device_usb = ", ".join([conn_device.name for conn_device in device.usb_connected])
        else:
            device_usb = ""
        if type(device) in [Computer, Laptop, Server, Router]:
            device_lan = ", ".join([conn_device.name for conn_device in device.local_connected])
        else:
            device_lan = ""
        if type(device) in [Laptop, Router, Phone, TV]:
            device_remote = ", ".join([conn_device.name for conn_device in device.remote_connected])
        else:
            device_remote = ""
        if type(device) in [Phone, Laptop, TV]:
            device_bluetooth = ", ".join([conn_device.name for conn_device in device.bluetooth_connected])
        else:
            device_bluetooth = ""
        device_vulnerabilities = ", ".join([vulnerability.name for vulnerability in device.vulnerabilities])
        print("------------------------------------")
        print(f"Type: {device_type}")
        print(f"Name: {device.name}")
        print(f"USB connected: {device_usb}")
        print(f"LAN connected: {device_lan}")
        print(f"Remote connected: {device_remote}")
        print(f"Bluetooth connected: {device_bluetooth}")
        print(f"Vulnerabilities: {device_vulnerabilities}")
        print("------------------------------------")


def get_device(name):
    return environment[[device.name for device in environment].index(name)]


def configure(set_device):
    if len(set_device) < 2:
        return 10
    if not check_name(set_device[0]):
        return 12
    cur_device = get_device(set_device[0])
    if set_device[1] == "name":
        if len(set_device) < 3:
            return 10
        if check_name(set_device[2]):
            return 9
        return cur_device.set_name(set_device[2])
    elif set_device[1] in "vulnerability":
        if len(set_device) < 4:
            return 10
        if set_device[2] == "add":
            return cur_device.set_vulnerability(set_device[3])
        elif set_device[2] == "del":
            return cur_device.del_vulnerability(set_device[3])
        else:
            return 13
    elif set_device[1] in ["usb", "lan", "bluetooth", "remote"]:
        if len(set_device) < 4:
            return 10
        if set_device[2] == "limit":
            try:
                set_device[3] = int(set_device[3])
            except ValueError:
                return 14
            try:
                if set_device[1] == "usb":
                    return cur_device.usb_set_limit(set_device[3])
                if set_device[1] == "lan":
                    return cur_device.local_set_limit(set_device[3])
                if set_device[1] == "bluetooth":
                    return cur_device.bluetooth_set_limit(set_device[3])
                if set_device[1] == "remote":
                    return cur_device.remote_set_limit(set_device[3])
            except AttributeError:
                return 14
        else:
            return 13
    else:
        return 13


def choose_option():
    while option := input("Сделать новую запись (1) или выбрать существующую(2)?: "):
        if eval(option) == 1:
            create_record()
            break
        if eval(option) == 2:
            open_record()
            break
        else:
            return 13


def get_result(code):
    if code == 0:
        return "Команда успешно выполнена"
    elif code == 1:
        return "Данный пораметр уже установлен на введённое значение"
    elif code == 2:
        return "Устройство уже включено"
    elif code == 3:
        return "Устройство уже выключено"
    elif code == 4:
        return "Устройство не подключено"
    elif code == 5:
        return "Устройство уже подключено"
    elif code == 6:
        return "Лимит подключений не установлен"
    elif code == 7:
        return "Достигнут лимит подключений"
    elif code == 8:
        return "Данное имя уже задано этому устройству"
    elif code == 9:
        return "Данное имя уже занято"
    elif code == 10:
        return "Недостаточно аргументов"
    elif code == 11:
        return "Тип устройства не найден"
    elif code == 12:
        return "Устройство не найдено"
    elif code == 13:
        return "Опция не найдена"
    elif code == 14:
        return "Неверная опция"
    elif code == 15:
        return "Неверный тип устройства"
    elif code == 16:
        return "Устройство уже находилось в пути пакета"


def connect(device):
    if len(device) < 3:
        return 10
    if not check_name(device[1]) and check_name(device[2]):
        return 12
    to_connect = get_device(device[1])
    connecting = get_device(device[2])
    if device[0] == "usb":
        if type(to_connect) not in [Computer, Laptop, Phone, Server] \
                and type(connecting) not in [Computer, Laptop, Phone, Server]:
            return 15
        return to_connect.usb_connect(get_device(device[2]))
    if device[0] == "lan":
        if type(to_connect) not in [Computer, Router, Server, Laptop] \
                and type(connecting) not in [Computer, Router, Server, Laptop]:
            return 15
        return to_connect.local_connect(get_device(device[2]))
    if device[0] == "bluetooth":
        if type(to_connect) not in [Phone, Laptop, TV] \
                and type(connecting) not in [Phone, Laptop, TV]:
            return 15
        return to_connect.bluetooth_connect(get_device(device[2]))
    if device[0] == "remote":
        if type(to_connect) not in [Router, Phone, TV, Laptop] \
                and type(connecting) not in [Router, Phone, TV, Laptop]:
            return 15
        return to_connect.remote_connect(get_device(device[2]))


def disconnect(device):
    if len(device) < 3:
        return 10
    if not check_name(device[1]) and check_name(device[2]):
        return 12
    to_connect = get_device(device[1])
    connecting = get_device(device[2])
    if device[0] == "usb":
        if type(to_connect) not in [Computer, Laptop, Phone, Server] \
                and type(connecting) not in [Computer, Laptop, Phone, Server]:
            return 15
        return to_connect.usb_disconnect(connecting)
    if device[0] == "lan":
        if type(to_connect) not in [Computer, Router, Server, Laptop] \
                and type(connecting) not in [Computer, Router, Server, Laptop]:
            return 15
        return to_connect.local_disconnect(connecting)
    if device[0] == "bluetooth":
        if type(to_connect) not in [Phone, Laptop, TV] \
                and type(connecting) not in [Phone, Laptop, TV]:
            return 15
        return to_connect.bluetooth_disconnect(connecting)
    if device[0] == "remote":
        if type(to_connect) not in [Router, Phone, TV, Laptop] \
                and type(connecting) not in [Router, Phone, TV, Laptop]:
            return 15
        return to_connect.remote_disconnect(connecting)


def trace(devices):
    if len(devices) < 2:
        return 12
    if not check_name(devices[0]) and not check_name(devices[1]):
        return 12
    from_device = get_device(devices[0])
    return from_device.send(devices[1], data="print trace")[0]


if __name__ == "__main__":
    if "db.sqlite" not in os.listdir("."):
        open("db.sqlite", "w")
    NAME = None
    environment = []
    vulnerabilities = []
    choose_option()
    while True:
        command = input("> ").strip().split()
        if command[0] == "delete":
            if len(command) < 2:
                print(get_result(10))
                continue
            print(get_result(delete(command[1])))
        elif command[0] == "exit":
            exit_program()
            break
        elif command[0] == "new":
            print(get_result(create(command[1:])))
        elif command[0] == "print":
            if len(command) > 1:
                if command[1] == "limits":
                    print_limits()
                else:
                    print(get_result(13))
            else:
                print_devices()
        elif command[0] == "set":
            print(get_result(configure(command[1:])))
        elif command[0] == "connect":
            print(get_result(connect(command[1:])))
        elif command[0] == "disconnect":
            print(get_result(disconnect(command[1:])))
        elif command[0] == "trace":
            print(get_result(trace(command[1:])))
        else:
            print("Команда не найдена")
