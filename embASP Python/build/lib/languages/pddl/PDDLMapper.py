from languages.Mapper import Mapper
class PDDLMapper(Mapper):
    __Instance = None

    def __init__(self):
        if PDDLMapper.__Instance:
            raise("Instance already exists")
        super().__init__()

    @classmethod
    def getInstance(cls):
        if not cls.__Instance:
            cls.__Instance = PDDLMapper()
        return cls.__Instance
    
    def _getActualString(self, predicate, parametersMap):
        return None
    
    def _getParameters(self, string):
        return string[string.index(" ") + 1:string.rfind(")")].split(" ")
    
    def _getPredicate(self, string):
        initialB = string.index("(")
        if initialB != 0:
            raise ("Wrong format")
        return string[1:string.index(" ")]
