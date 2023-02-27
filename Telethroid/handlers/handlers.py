class Handler:
    def __init__(self, callback: callable, filters=None):
        self.callback = callback
        self.filters = filters

class MsgHandler(Handler):
    def __init__(self, callback: callable, filters=None):
        super().__init__(callback, filters)

    def check(self, message):
        return (self.filters(message) if self.filterselse True)
