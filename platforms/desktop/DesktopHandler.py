from base.Handler import Handler

class DesktopHandler(Handler):
    
    def __init__(self, service):
        super(DesktopHandler, self).__init__()
        self.__service = service
        
    def startAsync(self, c, program_index=None, option_index=None):
        input_programs = self._collect_programs(program_index)
        input_options = self._collect_options(option_index)
        self.__service.startAsync(c, input_programs, input_options)
        
    def startSync(self, program_index=None, option_index=None):
        input_programs = self._collect_programs(program_index)
        input_options = self._collect_options(option_index)
        return self.__service.startSync(input_programs, input_options)
        
    