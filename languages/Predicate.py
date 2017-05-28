from abc import ABCMeta

class Predicate(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, terms):
        index = 0
        self.__mapTermsType = dict()
        for val in terms:
            if len(terms) > 1 and len(val) > 2 and isinstance(val, tuple):
                raise Exception("Bad definition of term")
            self.__mapTermsType[index] = val
            index += 1
    
#     @classmethod
#     @abstractmethod
#     def getPredicateName(cls):
#         pass
    
    @classmethod
    def getPredicateName(cls):
        return cls.predicateName
    
    def getTermsType(self):
        return self.__mapTermsType
    