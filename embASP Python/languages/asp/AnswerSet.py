class AnserSet:
    
    def __init__(self, value, weightMap=dict()):
        self.__value = value
        self.__weight_map = weightMap
        self.__atoms = None
        
    def getAnswerSet(self):
        return self.__value
    
    def getAtoms(self):
        if self.__atoms == None:
            #serve il mapper singleton
            pass
        return self.__atoms
    
    def getLevelWeight(self):
        return self.__weight_map
    
    def getWeights(self):
        return self.__weight_map
    
    def __str__(self):
        return str(self.__value)
    


