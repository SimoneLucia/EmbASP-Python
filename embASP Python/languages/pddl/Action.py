class Action(object):
    
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.name = name