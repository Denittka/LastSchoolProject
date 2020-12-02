class LAN:
    """
    Базовый класс для устройств с LAN.
    """
    def __init__(self):
        self.local_connected = []
        self.local_connection_limit = None

    def local_set_limit(self, num: int):
        """
        Устанавливает лимит подключений.
        :param num: число подключений
        :return: код ошибки
        """
        if self.local_connection_limit == num:
            return 1
        self.local_connection_limit = num
        return 0

    def local_connect(self, device):
        """
        Подключение устройства.
        :param device: имя устройтсва
        :return: код ошибки
        """
        if self.local_connection_limit is None or device.local_connection_limit is None:
            return 6
        if self.local_connection_limit == len(self.local_connected)\
                or device.local_connection_limit == len(device.local_connected):
            return 7
        if device in self.local_connected:
            return 5
        self.local_connected += [device]
        device.local_connected += [self]
        return 0

    def local_disconnect(self, device):
        """
        Отключение устройства.
        :param device: имя устройства
        :return: код ошибки
        """
        if device not in self.local_connected:
            return 4
        del self.local_connected[self.local_connected.index(device)]
        del device.local_connected[device.local_connected.index(self)]
        return 0
