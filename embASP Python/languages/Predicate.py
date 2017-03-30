from abc import ABC, abstractmethod
class Predicate(ABC):
    
    @classmethod
    @abstractmethod
    def getPredicateName(cls):
        pass