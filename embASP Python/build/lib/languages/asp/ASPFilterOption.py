from abc import ABC
from base.OptionDescriptor import OptionDescriptor

class ASPFilterOption(ABC, OptionDescriptor):
    def __init__(self):
        super().__init__("-filter=")