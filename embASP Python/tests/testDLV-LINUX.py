from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.dlv.desktop.DLVDesktopService import DLVDesktopService
from languages.asp.ASPInputProgram import ASPInputProgram
from specializations.dlv.DLVAnswerSets import DLVAnswerSets
from builtins import isinstance, input
from languages.Predicate import Predicate
from languages.asp.ASPMapper import ASPMapper
from languages.Predicate import Predicate
from base.Output import Output
from languages.asp.AnswerSets import AnswerSets
from base.OptionDescriptor import OptionDescriptor
import threading
from base.Callback import Callback
from specializations.dlv2.desktop.DLV2DesktopService import DLV2DesktopService


class CountDownLatch():
    def __init__(self, count=1):
        self.count = count
        self.lock = threading.Condition()

    def count_down(self):
        self.lock.acquire()
        self.count -= 1
        if self.count <= 0:
            self.lock.notifyAll()
        self.lock.release()

    def await(self):
        self.lock.acquire()
        while self.count > 0:
            self.lock.wait()
        self.lock.release()


























class Cell(Predicate):
      
    predicateName="cell"
    
    def __init__(self, row=None, column=None, value=None):
        super().__init__([("row", int), ("column", int), ("value", int)])
        self.row = row
        self.value = value
        self.column = column
          
#     @classmethod
#     def getPredicateName(cls):
#         return cls.predicateName
          
    def getRow(self):
        return self.row
    def getColumn(self):
        return self.column
    def getValue(self):
        return self.value
    def setRow(self, row):
        self.row = row
    def setColumn(self, column):
        self.column = column
    def setValue(self, value):
        self.value = value
        
        
        
lock = CountDownLatch(1)


        
        
w, h = 9, 9;
inputMatrix = [ [ 1, 0, 0, 0, 0, 7, 0, 9, 0 ],
                [ 0, 3, 0, 0, 2, 0, 0, 0, 8 ],
                [ 0, 0, 9, 6, 0, 0, 5, 0, 0 ],
                [ 0, 0, 5, 3, 0, 0, 9, 0, 0 ],
                [ 0, 1, 0, 0, 8, 0, 0, 0, 2 ],
                [ 6, 0, 0, 0, 0, 4, 0, 0, 0 ],
                [ 3, 0, 0, 0, 0, 0, 0, 1, 0 ],
                [ 0, 4, 1, 0, 0, 0, 0, 0, 7 ],
                [ 0, 0, 7, 0, 0, 0, 3, 0, 0 ] ]


# inputMatrix = [ [ 5, 0, 0, 0, 0, 0, 0, 8, 0 ],
#                 [ 0, 3, 0, 7, 0, 0, 0, 9, 0 ],
#                 [ 0, 0, 0, 4, 0, 2, 6, 0, 0 ],
#                 [ 6, 2, 0, 8, 0, 0, 3, 0, 0 ],
#                 [ 0, 9, 5, 0, 0, 0, 7, 1, 0 ],
#                 [ 0, 0, 1, 0, 0, 5, 0, 2, 6 ],
#                 [ 0, 0, 8, 5, 0, 3, 0, 0, 0 ],
#                 [ 0, 5, 0, 0, 0, 9, 0, 4, 0 ],
#                 [ 0, 1, 0, 0, 0, 0, 0, 0, 8 ] ]
            

handler = DesktopHandler(DLVDesktopService("app/src/test/resources/asp/executables/dlv.x86-64-linux-elf-static.bin"))
 
inp = ASPInputProgram()

for i in range(9):
    for j in range(9):
#         print(str(inputMatrix[i][j]) + " ", end="")
        if (inputMatrix[i][j] != 0):
            inp.addObjectInput(Cell(i,j,inputMatrix[i][j]))
#     print()
 
inp.addFilesPath("app/src/test/resources/asp/sudoku")
 
handler.addProgram(inp)



# out = handler.startSync()


class MyCalback(Callback):
    
    def __init__(self):
        self.ans=None
        self.lo = lock
    
    def callback(self, o):
        if (not isinstance(o, AnswerSets)):
            return
        self.ans = o
        self.lo.count_down()
    
    def getOutput(self):
        return self.ans



mc = MyCalback()

handler.startAsync(mc)

print("asincrono")

lock.await()

out = mc.getOutput()

mapp = ASPMapper.getInstance()


if not isinstance(out, Output):
    raise "error"


if (len(out.getAnswerSets()) != 0):
    ans = out.getAnswerSets()[0]
    
    Matrix = [[0 for x in range(w)] for y in range(h)] 
     
    for obj in ans.getAtoms():
        Matrix[obj.getRow()][obj.getColumn()] = obj.getValue()
     
    for i in range(9):
        for j in range(9):
            print(str(Matrix[i][j]), end=" ")
        print("")
else:
    print("output length = 0")          


