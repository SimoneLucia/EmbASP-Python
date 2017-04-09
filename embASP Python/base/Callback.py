from abc import ABC, abstractmethod

class Callback(ABC):
    
    @abstractmethod
    def callback(self, o):
        pass