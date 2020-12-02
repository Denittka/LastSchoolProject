class Bluetooth:
    """
    Базовый класс для устройтсв с Bluetooth.
    """
    def __init__(self):
        self.bluetooth_connected = []
        self.bluetooth_connection_limit = None

    def bluetooth_connect(self, device):
        """
        Подключает указанное устройство к текущему.
        :param device: имя подключаемого устройства
        :return: код ошибки
        """
        if self.bluetooth_connection_limit is None or device.bluetooth_connection_limit is None:
            return 6
        if self.bluetooth_connection_limit == len(self.bluetooth_connected)\
                or device.bluetooth_connection_limit == len(device.bluetooth_connected):
            return 7
        if device in self.bluetooth_connected:
            return 5
        self.bluetooth_connected += [device]
        device.bluetooth_connected += [self]
        return 0

    def bluetooth_disconnect(self, device):
        """
        Отключает указанное устройство от текущего.
        :param device: имя отключаемого устройства
        :return: код ошибки
        """
        if device not in self.bluetooth_connected:
            return 4
        del self.bluetooth_connected[self.bluetooth_connected.index(device)]
        del device.bluetooth_connected[device.bluetooth_connected.index(self)]
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
