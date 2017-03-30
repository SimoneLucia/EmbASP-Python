from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.dlv.desktop.DLVDesktopService import DLVDesktopService
from languages.asp.ASPInputProgram import ASPInputProgram
from specializations.dlv.DLVAnswerSets import DLVAnswerSets
from builtins import isinstance
from languages.Predicate import Predicate
from languages.asp import ASPMapper
from languages.asp.ASPMapper import ASPMapepr



class Uno(Predicate):
    
    PredicateName="uno"
    
    def __init__(self):
        self.uno="primo"
        self.due="secondo"
        
    @classmethod
    def getPredicateName(cls):
        return cls.PredicateName
    
    def getUno(self):
        return self.uno
    
    def getDue(self):
        return self.due
    
    def setUno(self, val):
        self.uno = val
        
    def setDue(self, val):
        self.due = val


un = Uno()

mapper = ASPMapepr.getInstance()

print(mapper.registerClass(Uno))

print(mapper._predicateClass)

print(mapper.getClass("uno"))

ob = mapper.getObject("uno(uno,due)")

print(ob.getDue())

print(ob.getUno())

print(mapper.unregisterClass(Uno))

print(mapper._predicateClass)

print(mapper.getString(un))

















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
