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

    def remote_connect(self, device):
        """
        Подключает устройство.
        :param device: имя устройства
        :return: код ошибки
        """
        if self.remote_connection_limit is not None and self.remote_connection_limit == len(self.remote_connected) \
                or device.remote_connection_limit is not None \
                and device.remote_connection_limit == len(device.remote_connected):
            return 7
        if device in self.remote_connected:
            return 5
        self.remote_connected += [device]
        device.remote_connected += [self]
        return 0

    def remote_disconnect(self, device):
        """
        Отключает устройство
        :param device: имя устройства
        :return: код ошибки
        """
        if device not in self.remote_connected:
            return 4
        del self.remote_connected[self.remote_connected.index(device)]
        del device.remote_connected[device.remote_connected.index(self)]
        return 0
