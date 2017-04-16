from languages.asp.ASPFilterOption import ASPFilterOption

class DLVFilterOption(ASPFilterOption):
    
    def __init__(self, initial_option):
        self._options += initial_option