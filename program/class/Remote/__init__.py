class Remote:
    def __init__(self):
        self.remote = []
        self.remote_count = 0

   def remote_set_count(self, count):
       if not isinstance(eval(count), int):
           return 9
       if not int(count) >= 0:
           return 10
       if len(self.remote) < int(count):
           return 12
       self.remote_count = int(count)
       return 0

    def remote_connect(self, device):
        if device in self.remote:
            return 9
        self.remote += [device]
        return 0

    def remote_disconnect(self, device):
        if device not in self.remote:
            return 10
        del self.remote[self.remote.index(device)]
        return 0
