class Calculator:

    def __init__(self,num_1,num_2,operator):
        self.__num_1 = num_1
        self.__num_2 = num_2
        self.__operator = operator

        self.__accumulator = 0
#Getters

    def get_operator(self):
        return self.__operator

    def get_accumulator(self):
        return self.__accumulator

    def get_num_1(self):
        return self.__num_1

    def get_num_2(self):
        return self.__num_2
#Setters
    def set_num_1(self, num):
        self.__num_1 = num

    def set_num_2(self, num):
        self.__num_2 = num

    def set_operator(self, op):
        self.__operator = op

    def set_accumulator(self):
        if self.get_operator() == '=':
            self.get_accumulator()

        elif self.get_operator() == '+':
            self.__accumulator = self.__num_1 + self.__num_2

        elif self.get_operator() == '-':
            self.__accumulator = self.__num_1 - self.__num_2

        elif self.get_operator() == '*':
            self.__accumulator = self.__num_1 * self.__num_2

        elif self.get_operator() == '/':
            self.__accumulator = self.__num_1 / self.__num_2

    def clear_accumulator(self):
        self.__accumulator = 0
