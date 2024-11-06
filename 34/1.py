class Public:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return f"hello{self.name}"


class Private:
    def __init__(self,numb):
        self.numb = numb

    def __privat(self):
        self.__numb

class Protected:
    def __init__(self,mer):
        self.mer = mer

    def _protected(self):
        self._mer