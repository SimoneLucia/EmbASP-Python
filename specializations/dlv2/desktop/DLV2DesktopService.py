from platforms.desktop.DesktopService import DesktopService
from base.OptionDescriptor import OptionDescriptor
from specializations.dlv2.DLV2AnswerSets import DLV2AnswerSets

class DLV2DesktopService(DesktopService):
    """Is an extention of DesktopService for DLV2's solver"""
    
    def __init__(self, exe_path):
        super(DLV2DesktopService, self).__init__(exe_path)
        self._load_from_STDIN_option = "--"
        self.competitionOutputOption = OptionDescriptor("--competition-output")
        
    def _getOutput(self, output, error):
        return DLV2AnswerSets(output, error)
    
    def startAsync(self, callback, programs, options):
        super(DLV2DesktopService, self).startAsync(callback, programs, options)
        
    def startSync(self, programs, options):
        options.append(self.competitionOutputOption)
        return super(DLV2DesktopService, self).startSync(programs, options)