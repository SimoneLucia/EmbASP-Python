from abc import ABCMeta
from base.OptionDescriptor import OptionDescriptor

class ASPFilterOption(OptionDescriptor):
    __metaclass__ = ABCMeta
    
    def __init__(self):
        super(ASPFilterOption, self).__init__("-filter=")