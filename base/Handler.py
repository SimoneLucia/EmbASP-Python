from abc import ABCMeta

class Handler(object):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self._programs = dict()
        self._options = dict()
        
    def addOption(self, o):
        last_index = len(self._options)
        current_value = last_index
        self._options[last_index]=o
        return current_value
    
    def addProgram(self, program):
        last_index = len(self._programs)
        current_value = last_index
        self._programs[last_index]=program
        return current_value
    
    def _collect_options(self, option_index):
        input_option = list()
        if (not option_index):
            for k in self._options.keys():
                input_option.append(self._options.get(k))
        else:
            for index in option_index:
                input_option.append(self._options.get(index))
        return input_option
    
    def _collect_programs(self, program_index):
        input_programs = list()
        if (not program_index):
            for k in self._programs.keys():
                input_programs.append(self._programs.get(k))
        else:
            for index in program_index:
                input_programs.append(self._programs.get(index))
        return input_programs
    
    def getInputProgram(self, key):
        return self._programs.get(key)
    
    def getOptionDescriptor(self, key):
        return self._options.get(key)
    
    def removeAll(self):
        self._options.clear()
        self._programs.clear()
        
    def removeOptionFromId(self, option_id):
        self._options.pop(option_id)
        
    def removeOptionFromValue(self, o):
        result=False
        for k in self._options:
            if(self._options.get(k) == o):
                self._options.pop(k)
                result=True
        return result
    
    def removeProgramFromValue(self, p):
        result=False
        for k in self._programs:
            if(self._programs.get(k) == p):
                self._programs.pop(k)
                result=True
        return result
    
    def removeProgramFromId(self, program_id):
        self._programs.pop(program_id)
        
    
    def startAsync(self, c, program_index=None, option_index=None):
        pass
    
    def startSync(self, program_index=None, option_index=None):
        return None
    
    
    
    