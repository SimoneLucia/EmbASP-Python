from abc import ABCMeta, abstractmethod

class Callback(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def callback(self, o):
        pass