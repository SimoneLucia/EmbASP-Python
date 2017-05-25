from base.InputProgram import InputProgram

class PDDLInputProgram(InputProgram):
    
    def __init__(self, progType):
        super(PDDLInputProgram, self).__init__()
        self.__programsType = progType
        
    def getProgramsType(self):
        return self.__programsType