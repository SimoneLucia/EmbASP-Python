from languages.Mapper import Mapper
class ASPMapper(Mapper):
    
    __Instance = None

    def __init__(self):
        if ASPMapper.__Instance:
            raise("Instance already exists")
        super().__init__()

    @classmethod
    def getInstance(cls):
        if not cls.__Instance:
            cls.__Instance = ASPMapper()
        return cls.__Instance
    
    def _getActualString(self, predicate, parametersMap):
        atom = predicate + "("
        for i in range(0,len(parametersMap)):
            if (i != 0):
                atom += ","
            objectTerm = parametersMap[i]
            if (objectTerm == None):
                raise("Wrong term number of predicate " + predicate)
            if (isinstance(objectTerm, int)):
                atom += str(objectTerm)
            else:
                atom += "\"" + str(objectTerm) + "\""
        atom += ")"
        return atom
    
    def _getParameters(self, string):
        return string[string.index("(")+1:string.index(")")].split(",")
    
    def _getPredicate(self, string):
        if "(" not in string:
            return string;
        return string[:string.index("(")]
        
        
        
        
            
        