
class ConfigsAdopter:
    __data = {}

    @classmethod
    def set(cls, key, value):
        cls.__data[key] = value
        return True

    @classmethod
    def get(cls, key):
        return cls.__data.get(key, None)

    @classmethod
    def get_all(cls):
        return cls.__data


