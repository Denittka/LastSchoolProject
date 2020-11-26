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
