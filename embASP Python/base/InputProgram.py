class InputProgram:
    
    def __init__(self):
        self._programs = None
        self.__files_paths = list()
        self._separator = " "


    def addObjectInput(self,inputObj):
        raise Exception("functionality not implemented")

    def addObjectsInput(self, inputObjs):
        for inputObj in inputObjs:
            self.addObjectInput(inputObj)

    def addFilesPath(self, file_path):
        self.__files_paths.append(file_path)


    def addProgram(self, new_instruction):
        if(self._programs == None):
            self._programs = new_instruction
        else:
            self._programs += self._separator + new_instruction

    def clearFilesPaths(self):
        del self.__files_paths[:]

    def clearPrograms(self):
        self._programs = None

    def clearAll(self):
        self.clearFilesPaths()
        self.clearPrograms()

    def getFilesPaths(self):
        return self.__files_paths

    def getPrograms(self):
        return self._programs

    def getSeparator(self):
        return self._separator

    def getStringOfFilesPaths(self):
        to_return=""
        for paths in self.__files_paths:
            if(len(paths) != 0):
                print(to_return)
                to_return += paths + " "
        return to_return

    def setPrograms(self, programs):
        self._programs = programs

    def setSeparator(self, separator):
        self._separator = separator


