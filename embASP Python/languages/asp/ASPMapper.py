from languages.Mapper import Mapper
class ASPMapepr(Mapper):
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise("Instance already exists")
        super().__init__()

    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = ASPMapepr()
        return cls.INSTANCE
    
    def _getActualString(self, predicate, parametersMap):
        atom = predicate + "("
        for i in range(0,len(parametersMap)):
            if (i != 0):
                atom += ","
            objectTerm = parametersMap[i]
            if (objectTerm == None):
                raise("Wrong term number of predicate " + predicate)
            if (isinstance(objectTerm, int)):
                atom += objectTerm + ""
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
        
        
        
        
            
        