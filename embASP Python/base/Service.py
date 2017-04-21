from abc import ABCMeta, abstractmethod

class Service(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def startAsync(self, callback, programs, options):
        pass
    
    @abstractmethod
    def startSync(self, programs, options):
        pass