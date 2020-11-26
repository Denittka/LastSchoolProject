class Remote:
    """
    Базовый класс для устройств с Wi-fi.
    """

    def __init__(self):
        self.remote_connected = []
        self.remote_connection_limit = None

    def remote_set_limit(self, num: int):
        """
        Устанавливает лимит подключений
        :param num: число подключений
        :return: код ошибки
        """
        if self.remote_connection_limit == num:
            return 1
        self.remote_connection_limit = num
        return 0

    def remote_connect(self, name: str):
        """
        Подключает устройство.
        :param name: имя устройства
        :return: код ошибки
        """
        if self.remote_connection_limit is None:
            return 6
        if self.remote_connection_limit == len(self.remote_connected):
            return 7
        if name in self.remote_connected:
            return 5
        self.remote_connected += [name]
        return 0

    def remote_disconnect(self, name: str):
        """
        Отключает устройство
        :param name: имя устройства
        :return: код ошибки
        """
        if name not in self.remote_connected:
            return 4
        del self.remote_connected[self.remote_connected.index(name)]
        return 0
