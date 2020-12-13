class Packet:
    def __init__(self, to_address, from_address, data):
        self.to_address = to_address
        self.from_address = from_address
        self.data = data
        self.last_address = from_address
        self.trace = []
