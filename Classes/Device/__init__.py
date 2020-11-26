class Device:
    """
    Базовый класс для всех устройств.
    """
    def __init__(self, name):
        self.name = name
        self.powered = False

    def power_on(self):
        """
        Включает устройство.
        :return: код ошибки
        """
        if self.powered:
            return 2
        self.powered = True
        return 0

    def power_off(self):
        """
        Выключает устройство.
        :return: код ошибки
        """
        if not self.powered:
            return 3
        self.powered = False
        return 0

    def send(self):
        pass

    def receive(self):
        pass
