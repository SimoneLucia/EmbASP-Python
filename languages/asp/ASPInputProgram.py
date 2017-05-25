from base.InputProgram import InputProgram
from languages.asp.ASPMapper import ASPMapper

class ASPInputProgram(InputProgram):
    
    def __init__(self):
        super(ASPInputProgram, self).__init__()
    
    
    #ci serve il mapper singleton
    
    def addObjectInput(self, inputObj):
        self.addProgram(ASPMapper.getInstance().getString(inputObj) + ".")
    
    
    def addObjectsInput(self, inputObjs):
        for inputObj in inputObjs:
            self.addObjectInput(inputObj)