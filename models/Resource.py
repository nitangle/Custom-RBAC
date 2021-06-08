class Resource:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return self.name
