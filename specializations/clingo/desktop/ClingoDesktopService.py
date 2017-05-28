from platforms.desktop.DesktopService import DesktopService
from specializations.clingo.ClingoAnswerSets import ClingoAnswerSets


class ClingoDesktopService(DesktopService):
    
    def __init__(self, exe_path):
        super(ClingoDesktopService, self).__init__(exe_path)
        self._load_from_STDIN_option = "-"
        
    def _getOutput(self, output, error):
        return ClingoAnswerSets(output, error)
    
    def startSync(self, programs, options):
        return super(ClingoDesktopService, self).startSync(programs, options)
    
    def startAsync(self, callback, programs, options):
        super(ClingoDesktopService, self).startAsync(callback, programs, options)