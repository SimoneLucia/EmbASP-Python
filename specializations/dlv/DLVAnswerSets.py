from languages.asp.AnswerSets import AnswerSets
from languages.asp.AnswerSet import AnserSet
import re

class DLVAnswerSets(AnswerSets):
    
    def __init__(self, out, err=None):
        super(DLVAnswerSets, self).__init__(out, err)
        
    def _parse(self):
        match = tuple(re.finditer(r"\{(.*)\}", self._output))
        for m in match:
            answerSet = m.group()
            answerSetList = set()
            matcherAnswerSet = tuple(re.finditer(r"(-?[a-z][A-Za-z0-9_]*(\(.+?\))?)(, |\})", answerSet))
            for ma in matcherAnswerSet:
                answerSetList.add(ma.group(1))
            self._answersets.append(AnserSet(answerSetList))
    

    
    
# output_example = "{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"r\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"r\")}"

# {node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"r\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"r\")}
