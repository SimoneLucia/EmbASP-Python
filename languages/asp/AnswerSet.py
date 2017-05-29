from languages.asp.ASPMapper import ASPMapper
class AnserSet(object):
    
    def __init__(self, value, weightMap=dict()):
        self.__value = value
        self.__weight_map = weightMap
        self.__atoms = set()
        
    def getAnswerSet(self):
        return self.__value
    
    def getAtoms(self):
        if not self.__atoms:
            mapper = ASPMapper.getInstance()
            for atom in self.__value:
                obj = mapper.getObject(atom)
                if (not obj == None):
                    self.__atoms.add(obj)
        return self.__atoms
    
    def getLevelWeight(self):
        return self.__weight_map
    
    def getWeights(self):
        return self.__weight_map
    
    def __str__(self):
        return str(self.__value)
    


