from languages.pddl.Plan import Plan
import json
from languages.pddl.Action import Action

class SPDPlan(Plan):
    
    def __init__(self, plan, error):
        super(SPDPlan, self).__init__(plan, error)
        
    def _parse(self):
        if self._errors != "" or self._output=="":
            return
        try:
            parsed_json = json.loads(self._output)
            status = parsed_json["status"]
            if "ok" in status:
                arrayPlan = parsed_json["result"]["plan"]
                for x in arrayPlan:
                    self._actionSequence.append(Action(x["name"]))
            else:
                self._errors += " " + parsed_json["result"]
                
        except ValueError as e:
            self._errors += "ParseException: " + e
    
    


# { "status": "ok","result": {"output": " --- OK. Match tree built with 40 nodes. PDDL problem description loaded:  Domain: BLOCKS  Problem: BLOCKS-4-0  #Actions: 40  #Fluents: 29 Landmarks found: 3 Starting search with IW (time budget is 60 secs)... rel_plan size: 6 #RP_fluents 10 Caption {#goals, #UNnachieved, #Achieved} -> IW(max_w) {3/3/0}:IW(1) -> [2][3]rel_plan size: 4 #RP_fluents 7 {3/2/1}:IW(1) -> [2][3]rel_plan size: 2 #RP_fluents 4 {3/1/2}:IW(1) -> [2][3]rel_plan size: 0 #RP_fluents 0Plan found with cost: -1.24904e+16 Total time: 0.000187 Nodes generated during search: 28 Nodes expanded during search: 9 IW search completed ",  "parse_status": "ok",  "type": "full",  "length": 6,  "plan": [  {   "action": " (:action pick-up :parameters (b) :precondition  (and   (clear b)   (ontable b)   (handempty)  ) :effect  (and   (not  (ontable b)   )   (not  (clear b)   )   (not  (handempty)   )   (holding b)  )  )",   "name": "(pick-up b)"  },  {   "action": " (:action stack :parameters (b a) :precondition  (and   (holding b)   (clear a)  ) :effect  (and   (not  (holding b)   )   (not  (clear a)   )   (clear b)   (handempty)   (on b a)  )  )",   "name": "(stack b a)"  },  {   "action": " (:action pick-up :parameters (c) :precondition  (and   (clear c)   (ontable c)   (handempty)  ) :effect  (and   (not  (ontable c)   )   (not  (clear c)   )   (not  (handempty)   )   (holding c)  )  )",   "name": "(pick-up c)"  },  {   "action": " (:action stack :parameters (c b) :precondition  (and   (holding c)   (clear b)  ) :effect  (and   (not  (holding c)   )   (not  (clear b)   )   (clear c)   (handempty)   (on c b)  )  )",   "name": "(stack c b)"  },  {   "action": " (:action pick-up :parameters (d) :precondition  (and   (clear d)   (ontable d)   (handempty)  ) :effect  (and   (not  (ontable d)   )   (not  (clear d)   )   (not  (handempty)   )   (holding d)  )  )",   "name": "(pick-up d)"  },  {   "action": " (:action stack :parameters (d c) :precondition  (and   (holding d)   (clear c)  ) :effect  (and   (not  (holding d)   )   (not (clear c) ) (clear d) (handempty) (on d c) ) )","name": "(stack d c)"}],"planPath": "/tmp/solver_planning_domains_tmp_45P1ERdUXBHwK/plan","logPath": "/tmp/solver_planning_domains_tmp_45P1ERdUXBHwK/log"}}

# str = '{ "status": "ok","result": {"output": " --- OK. Match tree built with 40 nodes. PDDL problem description loaded:  Domain: BLOCKS  Problem: BLOCKS-4-0  #Actions: 40  #Fluents: 29 Landmarks found: 3 Starting search with IW (time budget is 60 secs)... rel_plan size: 6 #RP_fluents 10 Caption {#goals, #UNnachieved, #Achieved} -> IW(max_w) {3/3/0}:IW(1) -> [2][3]rel_plan size: 4 #RP_fluents 7 {3/2/1}:IW(1) -> [2][3]rel_plan size: 2 #RP_fluents 4 {3/1/2}:IW(1) -> [2][3]rel_plan size: 0 #RP_fluents 0Plan found with cost: -1.24904e+16 Total time: 0.000187 Nodes generated during search: 28 Nodes expanded during search: 9 IW search completed ",  "parse_status": "ok",  "type": "full",  "length": 6,  "plan": [  {   "action": " (:action pick-up :parameters (b) :precondition  (and   (clear b)   (ontable b)   (handempty)  ) :effect  (and   (not  (ontable b)   )   (not  (clear b)   )   (not  (handempty)   )   (holding b)  )  )",   "name": "(pick-up b)"  },  {   "action": " (:action stack :parameters (b a) :precondition  (and   (holding b)   (clear a)  ) :effect  (and   (not  (holding b)   )   (not  (clear a)   )   (clear b)   (handempty)   (on b a)  )  )",   "name": "(stack b a)"  },  {   "action": " (:action pick-up :parameters (c) :precondition  (and   (clear c)   (ontable c)   (handempty)  ) :effect  (and   (not  (ontable c)   )   (not  (clear c)   )   (not  (handempty)   )   (holding c)  )  )",   "name": "(pick-up c)"  },  {   "action": " (:action stack :parameters (c b) :precondition  (and   (holding c)   (clear b)  ) :effect  (and   (not  (holding c)   )   (not  (clear b)   )   (clear c)   (handempty)   (on c b)  )  )",   "name": "(stack c b)"  },  {   "action": " (:action pick-up :parameters (d) :precondition  (and   (clear d)   (ontable d)   (handempty)  ) :effect  (and   (not  (ontable d)   )   (not  (clear d)   )   (not  (handempty)   )   (holding d)  )  )",   "name": "(pick-up d)"  },  {   "action": " (:action stack :parameters (d c) :precondition  (and   (holding d)   (clear c)  ) :effect  (and   (not  (holding d)   )   (not (clear c) ) (clear d) (handempty) (on d c) ) )","name": "(stack d c)"}],"planPath": "/tmp/solver_planning_domains_tmp_45P1ERdUXBHwK/plan","logPath": "/tmp/solver_planning_domains_tmp_45P1ERdUXBHwK/log"}}' 
# 
# parsed_json = json.loads(str)
# 
# a = parsed_json["result"]["plan"]
# 
# print(parsed_json)
# 
# for x in a:
#     print(x["name"])
#     
# print (parsed_json["status"])
