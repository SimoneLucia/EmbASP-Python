from abc import ABC, abstractmethod
class Predicate(ABC):
    
    def __init__(self, *terms):
        index = 0
        self.__map = dict()
        for value in terms:
            self.__map[index] = value
            index += 1
    
#     @classmethod
#     @abstractmethod
#     def getPredicateName(cls):
#         pass
    
    @classmethod
    def getPredicateName(cls):
        return cls.predicateName
    
    def getTerms(self):
        return self.__map