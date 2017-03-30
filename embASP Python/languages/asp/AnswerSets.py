from base.Output import Output

class AnswerSets(Output):
    
    def __init__(self, out, err=None):
        super().__init__(out, err)
        self._answersets = set()
        
    def getAnswerSets(self):
        if(not self._answersets):
            self._answersets = set()
            self._parse()
        return self._answersets
        
    def getAnswerSetsString(self):
        return self._output

