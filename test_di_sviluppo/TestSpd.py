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
    
    def get_output(self):
        return self.ans



class PickUp(Predicate):
      
    predicate_name="pick-up"
    
    def __init__(self, block=None):
        super(PickUp, self).__init__([("block")])
        self.block = block
          
    def get_block(self):
        return self.block
    
    def set_block(self, block):
        self.block = block
   

handler = DesktopHandler(SPDDesktopService())

inputProgramDomain = PDDLInputProgram(PDDLProgramType.DOMAIN)

inputProgramDomain.add_files_path("app/src/test/resources/pddl/blocksworld/domain.pddl")

inputProgramProblem = PDDLInputProgram(PDDLProgramType.PROBLEM)

inputProgramProblem.add_files_path("app/src/test/resources/pddl/blocksworld/p35.pddl")

handler.add_program(inputProgramDomain)
handler.add_program(inputProgramProblem)

PDDLMapper.get_instance().register_class(PickUp)


mc = MyCalback()

handler.start_async(mc)

print("asincrono")

lock.await()

res = mc.get_output()


# res = handler.start_sync()

for x in res.get_actions():
    print(x.get_name())

print("")

for x in res.get_actions_objects():
    print(x.get_block())
    







