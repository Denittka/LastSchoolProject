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

    def local_connect(self, name: str):
        """
        Подключение устройства.
        :param name: имя устройтсва
        :return: код ошибки
        """
        if self.local_connection_limit is None:
            return 6
        if self.local_connection_limit == len(self.local_connected):
            return 7
        if name in self.local_connected:
            return 5
        self.local_connected += [name]
        return 0

    def local_disconnect(self, name: str):
        """
        Отключение устройства.
        :param name: имя устройства
        :return: код ошибки
        """
        if name not in self.local_connected:
            return 4
        del self.local_connected[self.local_connected.index(name)]
        return 0
