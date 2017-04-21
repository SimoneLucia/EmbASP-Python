class PDDLException(Exception):
    def __init__(self, arg):
        super(PDDLException, self).__init__(arg)