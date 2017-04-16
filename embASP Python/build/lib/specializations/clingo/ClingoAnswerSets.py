from languages.asp.AnswerSets import AnswerSets
import re
from languages.asp.AnswerSet import AnserSet


class ClingoAnswerSets(AnswerSets):
    
    def __init__(self, out, err=None):
        super().__init__(out, err)
        
    def _parse(self):
        optimum = "OPTIMUM" in self._output
        
        if optimum:
            match = tuple(re.finditer(r"Answer: (d+)r?n(.*)", self._output))
        else:
            match = tuple(re.finditer(r"ANSWERr?n(.*)(r?nCOST (.+)r?nOPTIMUM)", self._output))
        
        for m in match:
            
            try:
                if match.group(1) == None or int(match.group(1)) <= len(self.answersets):
                    continue
            except Exception as e:
                print(e)
                break
            
            matcherAnswerSet = tuple(re.finditer(r"-?[a-z][A-Za-z0-9_]*((.*?))?", m.group(2)))
            answerSetList = list()
            
            for ma in matcherAnswerSet:
                answerSetList.append(ma.group())
                
            
            if optimum:
                weightMap = dict()
                try:
                    split = m.group(4).split(" ")
                    level = len(split)
                    for weight in split:
                        weightMap[level] = int(weight)
                        level-=1
                except Exception as e:
                    print (e)
                    
                self._answersets.append(AnserSet(answerSetList, weightMap))
                
            else:
                self._answersets.append(AnserSet(answerSetList))
            
            
            
            
            
            
            
            
            
            
            
                