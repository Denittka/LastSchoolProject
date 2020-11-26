class Bluetooth:
    """
    Базовый класс для устройтсв с Bluetooth.
    """
    def __init__(self):
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None

    def bluetooth_connect(self, name: str):
        """
        Подключает указанное устройство к текущему.
        :param name: имя подключаемого устройства
        :return: код ошибки
        """
        if self.bluetooth_connection_limit is None:
            return 6
        if self.bluetooth_connection_limit == len(self.bluetooth_connected):
            return 7
        if name in self.bluetooth_connected:
            return 5
        self.bluetooth_connected += [name]
        return 0

    def bluetooth_disconnect(self, name: str):
        """
        Отключает указанное устройство от текущего.
        :param name: имя отключаемого устройства
        :return: код ошибки
        """
        if name not in self.bluetooth_connected:
            return 4
        del self.bluetooth_connected[self.bluetooth_connected.index(name)]
        return 0

    def bluetooth_set_limit(self, num: int):
        """
        Устанавливает лимит подключений к Bluetooth.
        :param num: количество подключений
        :return: код ошибки
        """
        if self.bluetooth_connection_limit == num:
            return 1
        self.bluetooth_connection_limit = num
        return 0
