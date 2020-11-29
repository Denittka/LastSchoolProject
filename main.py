import os
from Classes.Computer import Computer
import sqlite3


def init_table(table_name):
    with sqlite3.connect("db.sqlite") as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name};")
        devices = cur.fetchall()
    for device in devices:
        new_device = None
        if device[1] == "computer":
            new_device = Computer()
        new_device.name = device[2]
        if type(device) in [Computer]:
            new_device.usb_connected = device[5].split(", ")
        if device in [Computer]:
            new_device.local_connected = device[3].split(", ")
        if device in []:
            new_device.remote_connected = device[4].split(", ")
        if device in []:
            new_device.bluetooth_connected = device[6].split(", ")
        device_vulnerabilities = device[7].split(", ")


def create_record():
    while True:
        name = input("Введите название записи: ")
        global NAME
        NAME = name
        print("Создание новой базы данных...")
        with sqlite3.connect("db.sqlite") as conn:
            cur = conn.cursor()
            try:
                cur.execute(f"CREATE TABLE {NAME} (ID INTEGER, type VARCHAR, name VARCHAR, LAN VARCHAR, \
                Remote VARCHAR, USB VARCHAR, Bluetooth VARCHAR, vulnerabilities VARCHAR, PRIMARY KEY(ID));")
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
    while num := eval(input("Какую запись открыть?: ")):
        if -1 < num - 1 < len(tables):
            print(f"Инициализируется запись {tables[num - 1][1]}...")
            init_table(tables[num - 1][1])
            print("Инициализация успешно завершена.")
            break
        else:
            print("Записи с таким номером не существует.")


def choose_option():
    while option := input("Сделать новую запись (1) или выбрать существующую(2)?: "):
        if eval(option) == 1:
            create_record()
            break
        if eval(option) == 2:
            open_record()
            break
        else:
            pass  # TODO


def exit_program():
    with sqlite3.connect("db.sqlite") as conn:
        cur = conn.cursor()
        for device in environment:
            if isinstance(device, Computer):
                device_type = "computer"
            if type(device) in [Computer]:
                device_usb = ", ".join(device.usb_connected)
            else:
                device_usb = ""
            if device in [Computer]:
                device_lan = ", ".join(device.local_connected)
            else:
                device_lan = ""
            if device in []:
                device_remote = ", ".join(device.remote_connected)
            else:
                device_remote = ""
            if device in []:
                device_bluetooth = ", ".join(device.bluetooth_connected)
            else:
                device_bluetooth = ""
            device_vulnerabilities = ", ".join(device.vulnerabilities)
            cur.execute(f"INSERT INTO {NAME} (type, name, usb, lan, remote, bluetooth, vulnerabilities) \
            VALUES ({device_type}, {device.name}, {device_usb}, {device_lan}, {device_remote}, {device_bluetooth}, \
            {device_vulnerabilities});")


def print_result(code):
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


if __name__ == "__main__":
    if "db.sqlite" not in os.listdir("."):
        open("db.sqlite", "w")
    NAME = None
    environment = []
    choose_option()
    while True:
        command = input("> ").strip()
        if command == "exit":
            exit_program()
            break  # TODO
