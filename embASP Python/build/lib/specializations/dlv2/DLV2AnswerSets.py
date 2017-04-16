from languages.asp.AnswerSets import AnswerSets
import re
from languages.asp.AnswerSet import AnserSet


class DLV2AnswerSets(AnswerSets):
    
    def __init__(self, out, err=None):
        super().__init__(out, err)
        
    def _parse(self):
        optimum = "OPTIMUM" in self._output
        
        if optimum:
            match = tuple(re.finditer(r"ANSWERr?n(.*)", self._output))
        else:
            match = tuple(re.finditer(r"ANSWERr?n(.*)(r?nCOST (.+)r?nOPTIMUM)", self._output))
        
        for m in match:
            matcherAnswerSet = tuple(re.finditer(r"-?[a-z][A-Za-z0-9_]*((.*?))?", m.group(1)))
            answerSetList = list()
            
            for ma in matcherAnswerSet:
                answerSetList.append(ma.group())
                
            if optimum:
                weightMap = dict()
                try:
                    split = m.group(3).split(" ")
                    for weightLevel in split:
                        weightLevelArray = weightLevel.split("@")
                        weightMap[weightLevelArray[1]] = weightLevelArray[0]
                except Exception as e:
                    print (e)
                
                self._answersets.append(AnserSet(answerSetList, weightMap))    
                
            else:
                self._answersets.append(AnserSet(answerSetList))
                
                