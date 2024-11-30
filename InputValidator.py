from abc import ABC,abstractmethod
class UserInputs(ABC):

    @abstractmethod
    def validate_positive_integer(self):
        pass
class UserInputValidator(UserInputs):
    def __init__(self,dataset):
        self.__dataset = dataset
        self.__newlist = []
    
    def inputsarevalidated(self):
         print("The list is validated")
    
    def validate_positive_integer(self):

        for row in self.__dataset:
            if int(row) >= 0:
                    self.__newlist.append(row)
            else:
                 pass
        print(self.inputsarevalidated())    
        print(self.__newlist)
                    
list = [1,2,3,-1,-2,-3,4,5,6,7,-2]
s1 = UserInputValidator(list)
s1.validate_positive_integer()