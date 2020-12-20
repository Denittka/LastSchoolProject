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

    def usb_connect(self, device):
        """
        Подключает устройство.
        :param device: имя устройства
        :return: код ошибки
        """
        if self.usb_connection_limit is not None or device.usb_connection_limit is not None:
            return 6
        if self.usb_connection_limit is not None and self.usb_connection_limit == len(self.usb_connected)\
                or device.usb_connection_limit is not None and device.usb_connection_limit == len(device.usb_connected):
            return 7
        if device in self.usb_connected:
            return 5
        self.usb_connected += [device]
        device.usb_connected += [self]
        return 0

    def usb_disconnect(self, device):
        """
        Отключает устройство
        :param device: имя устройства
        :return: код ошибки
        """
        if device not in self.usb_connected:
            return 4
        del self.usb_connected[self.usb_connected.index(device)]
        del device.usb_connected[device.usb_connected.index(self)]
        return 0
