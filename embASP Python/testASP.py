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
        super().__init__("row", "column", "value")
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
            

handler = DesktopHandler(DLVDesktopService("app/src/test/resources/asp/executables/dlv.mingw.exe"))
 
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



if not isinstance(out, Output):
    raise "error"

if (len(out.getAnswerSets()) != 0):
    ans = out.getAnswerSets()[0]
    
    Matrix = [[0 for x in range(w)] for y in range(h)] 
     
    for obj in ans.getAtoms():
        obj.__class__ = Cell
        Matrix[int(obj.getRow())][int(obj.getColumn())] = obj.getValue()
     
    for i in range(9):
        for j in range(9):
            print(str(Matrix[i][j]), end=" ")
        print("")
                





# class Test(Predicate):
#     
#     __predicateName="test"
#     
#     def __init__(self):
#         super().__init__("uno", "due")
#         self.due = "ciccio"
#         self.uno = "franco"
#         
#     @classmethod
#     def getPredicateName(cls):
#         return cls.__predicateName
#         
#     def getUno(self):
#         return self.uno
#     def getDue(self):
#         return self.due
#     def setUno(self, uno):
#         self.uno = uno
#     def setDue(self, due):
#         self.due = due
# 
# t = Test()
# 
# mapper = ASPMapper.getInstance()
#  
# print(mapper.registerClass(Test))
#  
# print(mapper._predicateClass)
#  
# print(mapper.getClass("test"))
#  
# ob = mapper.getObject("test(aaa,bbb)")
#  
# print(ob.getDue())
#  
# print(ob.getUno())
#  
# print(mapper.unregisterClass(Test))
#  
# print(mapper._predicateClass)
#  
# print(mapper.getString(t))

















# class Uno(Predicate):
#     
#     PredicateName="uno"
#     
#     def __init__(self):
#         self.uno="primo"
#         self.due="secondo"
#         
#     @classmethod
#     def getPredicateName(cls):
#         return cls.PredicateName
#     
#     def getUno(self):
#         return self.uno
#     
#     def getDue(self):
#         return self.due
#     
#     def setUno(self, val):
#         self.uno = val
#         
#     def setDue(self, val):
#         self.due = val
# 
# 
# un = Uno()
# 
# mapper = ASPMapepr.getInstance()
# 
# print(mapper.registerClass(Uno))
# 
# print(mapper._predicateClass)
# 
# print(mapper.getClass("uno"))
# 
# ob = mapper.getObject("uno(uno,due)")
# 
# print(ob.getDue())
# 
# print(ob.getUno())
# 
# print(mapper.unregisterClass(Uno))
# 
# print(mapper._predicateClass)
# 
# print(mapper.getString(un))















# ---------INTROSPECTION---------
# hand = DesktopHandler(DLVDesktopService("niente"))
# print(hand.__class__.__name__)


# hand = DesktopHandler(DLVDesktopService("niente"))
#  
# ip = ASPInputProgram()
#  
# bo = set()
#  
# ip.addObjectInput(bo)
#  
# ip.addFilesPath("---")
#  
# hand.addProgram(ip)
# 
# # ma = DLVAnswerSets
# 
# out = hand.startSync()
# 
# print(out.getAnswerSets())

# ma = hand.startSync()


# tt = ma.getAnswersets()
# ma.getAnswersets()

# 
# test = DLVAnswerSets("cf")
# 
# print(test.getAnswersets())





# d = DLVAnswerSets("{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"r\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"r\")}")
# lista = d.getAnswerSets()
# for l in lista:
#     for t in l.getAnswerSet():
#         print(t)



# field = "mioMetodo"
# 
# print("get" + field[:1].upper() + field[1:])











# class A:
#     def __init__(self):
#         self.uno = "uno"
#     def tes(self):
#         print(self.uno)
#         
# asp = A
# aa = A()
# m = getattr(asp, "tes")
# 
# getattr(aa, m)()
        
        
        
# class B(A):
#     def __init__(self):
# #         A.__init__(self)
#         self.due = "due"
#         self.tre = "tre"
#         self.a = "a"
#         self.cacca = "cacca"
# class C:
#     def __init__(self):
#         pass
# #         
# b = B
# 
# print( isinstance(b, A))

# 
# print(b.__dict__)



# class Test(Predicate):
#     def __init__(self):
#         self.uno="uno"
#     
#     def getPredicateName(self):
#         return "test"
# 
# t = Test()







# class A(object):
#     foobar = 42
#     def __init__(self):
#         self.foo = 'baz'
#         self.bar = 3
#     def method(self, arg):
#         return True
# 
# 
# 
# 
# a = A()
# 
# res = getattr(a, "method")("--")
# 
# print(res)

# print(set(a.__dict__.keys()))
# print(vars(a))





# from languages.asp.ASPInputProgram import ASPInputProgram
# from specializations.dlv.desktop.DLVDesktopService import DLVDesktopService
# from base.Service import Service
# from base import InputProgram
# from base.testImp import test
# 
# 
# 
# 
# 
# tt = ASPInputProgram()
# 
# 
# tt.addObjectInput("test")
# 
#  
# # inp = ASPInputProgram()
# # 
# # ina = ["uno", "due", "tre"]
# # 
# # inp.addObjectsInput(ina)
# 
# #  
# # test = test()
# #  
# # test.addFilesPath("madre")
# #  
# # test.addFilesPath("di")
# #  
# # test.addFilesPath("dio")
# #  
# # #test.clearFilesPaths();
# #  
# # test.addProgram("test di dio")
# #  
# # test.addProgram("madonnina")
# #  
# # #test.clearPrograms()
# #  
# # #test.clearAll()
# #  
# # ##test.get()
# #  
# # ##test.getdu()
# # 
# #  
# # a = ["asd", "asddd", "asddef"]
# #  
# #  
# #  
# #  
# # test.addObjectInput("aaa")






# from specializations.dlv.DLVAnswerSets import DLVAnswerSets
# 
# dl = DLVAnswerSets("---")
# dl.setOutput("{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"b\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"r\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"r\"), color(\"nodo3\",\"g\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"g\"), color(\"nodo2\",\"b\"), color(\"nodo3\",\"r\")}\n\n{node(\"nodo1\"), node(\"nodo2\"), node(\"nodo3\"), arc(\"nodo1\",\"nodo2\"), arc(\"nodo2\",\"nodo3\"), arc(\"nodo3\",\"nodo1\"), color(\"nodo1\",\"b\"), color(\"nodo2\",\"g\"), color(\"nodo3\",\"r\")}")    
# dl._parse()
# for k in dl.getAnswersets():
#     for j in k.getAnswerSet():
#         print(j)
