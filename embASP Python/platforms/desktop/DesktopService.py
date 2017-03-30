from base.Service import Service
from abc import abstractmethod

class DesktopService(Service):
    
    def __init__(self, exe_path):
        self._exe_path = exe_path
        _load_from_STDIN_option = None
        
    def getExePath(self):
        return self._exe_path
    
    @abstractmethod
    def _getOutput(self, output, error):
        pass
    
    def setExePath(self, exe_path):
        self._exe_path = exe_path
    
    def startAsync(self, callback, programs, options):
        #TODO
        pass
    
    def startSync(self, programs, options):
        #TODO
        return self._getOutput("", "")
    
