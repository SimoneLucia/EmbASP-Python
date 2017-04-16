from platforms.desktop.DesktopHandler import DesktopHandler
from specializations.solver_planning_domains.desktop.SPDDesktopService import SPDDesktopService
from languages.pddl.PDDLInputProgram import PDDLInputProgram
from languages.pddl.PDDLProgramType import PDDLProgramType
from languages.Predicate import Predicate
from languages.pddl.PDDLMapper import PDDLMapper
from languages.pddl.Plan import Plan
from base.Callback import Callback
import threading

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





lock = CountDownLatch(1)

class MyCalback(Callback):
    
    def __init__(self):
        self.ans=None
        self.lo = lock
    
    def callback(self, o):
        if (not isinstance(o, Plan)):
            return
        self.ans = o
        self.lo.count_down()
    
    def getOutput(self):
        return self.ans



class PickUp(Predicate):
      
    predicateName="pick-up"
    
    def __init__(self, block=None):
        super().__init__([("block")])
        self.block = block
          
#     @classmethod
#     def getPredicateName(cls):
#         return cls.predicateName
          
    def getBlock(self):
        return self.block
    
    def setBlock(self, block):
        self.block = block
   






handler = DesktopHandler(SPDDesktopService())

inputProgramDomain = PDDLInputProgram(PDDLProgramType.DOMAIN)

inputProgramDomain.addFilesPath("app/src/test/resources/pddl/blocksworld/domain.pddl")

inputProgramProblem = PDDLInputProgram(PDDLProgramType.PROBLEM)

inputProgramProblem.addFilesPath("app/src/test/resources/pddl/blocksworld/p35.pddl")

handler.addProgram(inputProgramDomain)
handler.addProgram(inputProgramProblem)

PDDLMapper.getInstance().registerClass(PickUp)





mc = MyCalback()

handler.startAsync(mc)

print("asincrono")

lock.await()

res = mc.getOutput()


# res = handler.startSync()

for x in res.getActions():
    print(x.getName(), end=", ")

print("")

for x in res.getActionsObjects():
    print(x.getBlock(), end=", ")
    







