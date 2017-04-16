class OptionDescriptor:
    
    def __init__(self, initial_option=None):
        self._options = initial_option
        self._separator = ""
        
    def addOption(self, option):
        if (self._options == None or self._options == ""):
            self.setOptions(option)
        else:
            self._options += self._separator + option
    
    def clear(self):
        self._options = ""
        
    def getOptions(self):
        return self._options
    
    def getSeparator(self):
        return self._separator
    
    def setOptions(self, option):
        self._options = option
        
    def setSeparator(self, separator):
        self._separator = separator
    