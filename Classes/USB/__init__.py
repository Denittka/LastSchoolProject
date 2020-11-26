class USB:
    """
    Базовый класс для устройств с USB.
    """

    def __init__(self):
        self.usb_connected = []
        self.usb_connection_limit = None

    def usb_set_limit(self, num: int):
        """
        Устанавливает лимит подключений
        :param num: число подключений
        :return: код ошибки
        """
        if self.usb_connection_limit == num:
            return 1
        self.usb_connection_limit = num
        return 0

    def usb_connect(self, name: str):
        """
        Подключает устройство.
        :param name: имя устройства
        :return: код ошибки
        """
        if self.usb_connection_limit is None:
            return 6
        if self.usb_connection_limit == len(self.usb_connected):
            return 7
        if name in self.usb_connected:
            return 5
        self.usb_connected += [name]
        return 0

    def usb_disconnect(self, name: str):
        """
        Отключает устройство
        :param name: имя устройства
        :return: код ошибки
        """
        if name not in self.usb_connected:
            return 4
        del self.usb_connected[self.usb_connected.index(name)]
        return 0
