from platforms.desktop.desktop_handler import DesktopHandler
from specializations.dlv.desktop.dlv_desktop_service import DLVDesktopService
from languages.asp.asp_input_program import ASPInputProgram
from specializations.dlv.dlv_answer_sets import DLVAnswerSets
from languages.predicate import Predicate
from languages.asp.asp_mapper import ASPMapper
from base.output import Output
from languages.asp.answer_sets import AnswerSets
from base.option_descriptor import OptionDescriptor
import threading
from base.callback import Callback
from specializations.dlv2.desktop.dlv2_desktop_service import DLV2DesktopService


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
      
    predicate_name="cell"
    
    def __init__(self, row=None, column=None, value=None):
        super(Cell, self).__init__([("row", int), ("column", int), ("value", int)])
        self.row = row
        self.value = value
        self.column = column
          
    def get_row(self):
        return self.row
    def get_column(self):
        return self.column
    def get_value(self):
        return self.value
    def set_row(self, row):
        self.row = row
    def set_column(self, column):
        self.column = column
    def set_value(self, value):
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



handler = DesktopHandler(DLV2DesktopService("app/src/test/resources/asp/executables/dlv2"))
 
inp = ASPInputProgram()

for i in range(9):
    for j in range(9):
#         print(str(inputMatrix[i][j]) + " ", end="")
        if (inputMatrix[i][j] != 0):
            inp.add_object_input(Cell(i,j,inputMatrix[i][j]))
#     print()
 
inp.add_files_path("app/src/test/resources/asp/sudoku")
 
handler.add_program(inp)



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
    
    def get_output(self):
        return self.ans



mc = MyCalback()

handler.start_async(mc)

print("asincrono")

lock.await()

out = mc.get_output()

mapp = ASPMapper.get_instance()


if not isinstance(out, Output):
    raise "error"


if (len(out.get_answer_sets()) != 0):
    ans = out.get_answer_sets()[0]
    
    Matrix = [[0 for x in range(w)] for y in range(h)] 
     
    for obj in ans.get_atoms():
        Matrix[obj.get_row()][obj.get_column()] = obj.get_value()
     
    tmp=""
    for i in range(9):
        for j in range(9):
            tmp += str(Matrix[i][j]) + " "
        print(tmp)
        tmp=""
else:
    print("output length = 0")          

