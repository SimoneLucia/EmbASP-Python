


# -----------NON HO USATO LA CLASSE SPDUTILITY, MA HO SCRITTO I METODI DI UTILITà DIRETTAMENTE NELLA CLASSE SPDDESKTOPSERVICE------------

# from abc import ABC, abstractmethod
# from languages.pddl.PDDLInputProgram import PDDLInputProgram
# from languages.pddl.PDDLProgramType import PDDLProgramType
# import json
# import traceback
# import http.client
# 
# 
# class SPDUtility(ABC):
#     
#     def __init__(self):
#         self.__solverUrl = "solver.planning.domains"
#     
#     def createJson(self, pddlInputProgram):
#         problem = ""
#         domain = ""
#         
#         for ip in pddlInputProgram:
#             if not isinstance(pddlInputProgram, PDDLInputProgram):
#                 continue
#             pip = ip
#             pType = pip.getProgramsType()
#             if pType is PDDLProgramType.DOMAIN:
#                 domain += pip.getPrograms() + pip.getSeparator()
#                 domain += self.getFromFile(pip.getFilesPaths(), pip.getSeparator())
#             elif pType is PDDLProgramType.PROBLEM:
#                 problem += pip.getPrograms() + pip.getSeparator()
#                 problem += self.getFromFile(pip.getFilesPaths(), pip.getSeparator())
#             else:
#                 raise ("Program type : " + pip.getProgramsType() + " not valid.")
#             
#         if problem == "":
#             raise ("Problem file not specified")
#         if domain == "":
#             raise("Domain file not specified")
#         
#         data = {}
#         data["problem"] = problem
#         data["domain"] = domain
#         
#         json_data = json.dumps(data)
#         
#         return json_data
#         
#                 
#     def __getFromFile(self, filesPaths, separator):
#         toReturn = ""
#         for s in filesPaths:
#             try:
#                 toReturn += self.readFile(s)
#                 toReturn += separator
#             except IOError:
#                 traceback.print_exc()
#         return toReturn
#     
#     
#     def postJsonToURL(self, jsonaa):
#         js = json.dumps(jsonaa)
#         result = ""
#         try:
#             connection = http.client.HTTPConnection(self.__solverUrl)
#             headers = {'Content-type': 'application/json'}
#             
#             connection.request('POST', '/solve', js, headers)
#             
#             response = connection.getresponse()
#             print(response.status)
#             if response.status == 200:
#                 result = response.read().decode()
#             else:
#                 raise PDDLException("HTTP connection error, response code : " + str(response.status) + " response message : " + str(response.reason))
#         except:
#             raise PDDLException("Impossible to perform HTTP connection")
#         return result
#     
#     
#     @abstractmethod
#     def _readFile(self, s):
#         pass
#         
#         
# # a = SPDUtility()
# # 
# # dic = {"problem":" (define (problem BLOCKS-4-0)\r\n(:domain BLOCKS)\r\n(:objects D B A C - block)\r\n(:INIT (CLEAR C) (CLEAR A) (CLEAR B) (CLEAR D) (ONTABLE C) (ONTABLE A)\r\n (ONTABLE B) (ONTABLE D) (HANDEMPTY))\r\n(:goal (AND (ON D C) (ON C B) (ON B A)))\r\n)\r\n ","domain":" ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\r\n;;; 4 Op-blocks world\r\n;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;\r\n\r\n(define (domain BLOCKS)\r\n  (:requirements :strips :typing)\r\n  (:types block)\r\n  (:predicates (on ?x - block ?y - block)\r\n\t       (ontable ?x - block)\r\n\t       (clear ?x - block)\r\n\t       (handempty)\r\n\t       (holding ?x - block)\r\n\t       )\r\n\r\n  (:action pick-up\r\n\t     :parameters (?x - block)\r\n\t     :precondition (and (clear ?x) (ontable ?x) (handempty))\r\n\t     :effect\r\n\t     (and (not (ontable ?x))\r\n\t\t   (not (clear ?x))\r\n\t\t   (not (handempty))\r\n\t\t   (holding ?x)))\r\n\r\n  (:action put-down\r\n\t     :parameters (?x - block)\r\n\t     :precondition (holding ?x)\r\n\t     :effect\r\n\t     (and (not (holding ?x))\r\n\t\t   (clear ?x)\r\n\t\t   (handempty)\r\n\t\t   (ontable ?x)))\r\n  (:action stack\r\n\t     :parameters (?x - block ?y - block)\r\n\t     :precondition (and (holding ?x) (clear ?y))\r\n\t     :effect\r\n\t     (and (not (holding ?x))\r\n\t\t   (not (clear ?y))\r\n\t\t   (clear ?x)\r\n\t\t   (handempty)\r\n\t\t   (on ?x ?y)))\r\n  (:action unstack\r\n\t     :parameters (?x - block ?y - block)\r\n\t     :precondition (and (on ?x ?y) (clear ?x) (handempty))\r\n\t     :effect\r\n\t     (and (holding ?x)\r\n\t\t   (clear ?y)\r\n\t\t   (not (clear ?x))\r\n\t\t   (not (handempty))\r\n\t\t   (not (on ?x ?y)))))\r\n "}
# # 
# # print(a.postJsonToURL(dic))
# 


