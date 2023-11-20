import pickle


class DAO():
    def __init__(self, datasource='') -> None:
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __load(self):
        with open(self.__datasource, 'rb') as file:
            self.__cache = pickle.load(file)

    def __dump(self):
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__cache, file)

    def add(self, key, obj):
        if key in self.__cache:
            raise KeyError
        self.__cache[key] = obj
        # self.__dump()

    def get(self, key):
        if key in self.__cache:
            return self.__cache[key]
        raise KeyError

    def remove(self, key):
        if key in self.__cache:
            self.__cache.pop(key)
            # self.__dump()
            return
        raise KeyError

    def get_all(self):
        return self.__cache.values()
