from base.Output import Output

class AnswerSets(Output):
    
    def __init__(self, out, err=None):
        super(AnswerSets, self).__init__(out, err)
        self._answersets = None
        
    def getAnswerSets(self):
        if(self._answersets == None):
            self._answersets = list()
            self._parse()
        return self._answersets
        
    def getAnswerSetsString(self):
        return self._output

