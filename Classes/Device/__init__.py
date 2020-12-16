class Device:
    """
    Базовый класс для всех устройств.
    """
    def __init__(self):
        self.name = None
        self.powered = False
        self.vulnerabilities = []

    def set_name(self, name):
        if self.name == name:
            return 8
        self.name = name
        return 0

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

    def send(self, to_address, data):
        pass

    def receive(self, from_address, packet):
        if packet.to_address == self.name:
            return [self.do(packet.data, packet), packet]
        if self.name in packet.trace:
            return [16, packet]
        packet.add_to_trace(self.name)
        return self.send(packet.to_address, packet=packet)

    def do(self, command):
        pass
