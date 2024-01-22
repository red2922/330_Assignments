class Flower:
    def __init__(self,name, petals, price):
        self.__name = str(name)
        self.__petals = int(petals)
        self.__price = float(price)

    #Getters
    def get_name(self):
        return self.__name

    def get_petals(self):
        return self.__petals

    def get_price(self):
        return self.__price

    #Setters
    def set_name(self, new_name):
        self.__name = new_name

    def set_petals(self, new_petals):
        self.__petals = new_petals

    def set_price(self, new_price):
        self.__price = new_price