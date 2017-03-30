from abc import ABC, abstractmethod

class Service(ABC):
    
    @abstractmethod
    def startAsync(self, callback, programs, options):
        pass
    
    @abstractmethod
    def startSync(self, programs, options):
        pass