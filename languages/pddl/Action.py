class Action(object):
    """Represent a generic Action"""
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.name = name