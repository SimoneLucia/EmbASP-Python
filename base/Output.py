class Output(object):
    
    def __init__(self, output=None, errors=None):
        self._output = output
        self._errors = errors
    
    def getErrors(self):
        return self._errors
    
    def getOutput(self):
        return self._output
    
    def setErrors(self, errors):
        self._errors=errors
        
    def setOutput(self, output):
        self._output=output

    def _parse(self):
        pass