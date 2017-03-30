from base.InputProgram import InputProgram

class ASPInputProgram(InputProgram):
    
    def __init__(self):
        super().__init__()
    
    
    #ci serve il mapper singleton
    
    def addObjectInput(self, inputObj):
        InputProgram.addProgram(self, inputObj)
    
    
    
    
    
    
    def addObjectsInput(self, inputObjs):
        for inputObj in inputObjs:
            self.addObjectInput(inputObj)