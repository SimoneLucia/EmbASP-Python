from base.Service import Service
from abc import abstractmethod
from base.OptionDescriptor import OptionDescriptor
from base.InputProgram import InputProgram
from base.Output import Output
import subprocess
import time
from threading import Thread

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
        
        class myThread(Thread):
            def __init__(self, startSync):
                Thread.__init__(self)
                self.startSync = startSync
            def run(self):
                callback.callback(self.startSync(programs, options))
                 
        th = myThread(self.startSync)
        th.start()
        

    
    def startSync(self, programs, options):
        option = ""
        for o in options:
            if(o != None):
                option += o.getOptions()
                option += o.getSeparator()
            else:
                print("Warning : wrong " + str(OptionDescriptor().__class__.__name__))
        files_paths = ""
        final_program = ""
        for p in programs:
            if (p != None):
                final_program += p.getPrograms()
                program_file = p.getStringOfFilesPaths()
                if (program_file != None):
                    files_paths += program_file
            else:
                print("Warning : wrong " + str(InputProgram().__class__.__name__))
                
        if (self._exe_path == None):
            return Output("", "Error: executable not found");
        
        exep = str(self._exe_path)
        
        opt = str(option)
        
        lis = list()
        lis.append(exep)
        if opt != "":
            lis.append(opt)
        lis.append(files_paths[:-1])
        if self._load_from_STDIN_option != "":
            lis.append(self._load_from_STDIN_option)
        
        print(exep + " " + opt + " " + files_paths + self._load_from_STDIN_option)
        
        start = int(time.time()*1e+9)
        
        proc = subprocess.Popen(lis, universal_newlines=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, )
        
        output, error = proc.communicate(final_program)
        
        end = int(time.time()*1e+9)
        
        print("time: " + str(end - start))
        
        return self._getOutput(output, error)
        
        
        #TODO
#         return self._getOutput("[build BEN/Dec 17 2012   gcc 4.6.1]\n\n{sizeBlock(3), pos(0), pos(1), pos(2), pos(3), pos(4), pos(5), pos(6), pos(7), pos(8), symbol(1), symbol(2), symbol(3), symbol(4), symbol(5), symbol(6), symbol(7), symbol(8), symbol(9), cell(0,0,1), cell(0,5,7), cell(0,7,9), cell(1,1,3), cell(1,4,2), cell(1,8,8), cell(2,2,9), cell(2,3,6), cell(2,6,5), cell(3,2,5), cell(3,3,3), cell(3,6,9), cell(4,1,1), cell(4,4,8), cell(4,8,2), cell(5,0,6), cell(5,5,4), cell(6,0,3), cell(6,7,1), cell(7,1,4), cell(7,2,1), cell(7,8,7), cell(8,2,7), cell(8,6,3), assigned(0,0), assigned(0,5), assigned(0,7), assigned(1,1), assigned(1,4), assigned(1,8), assigned(2,2), assigned(2,3), assigned(2,6), assigned(3,2), assigned(3,3), assigned(3,6), assigned(4,1), assigned(4,4), assigned(4,8), assigned(5,0), assigned(5,5), assigned(6,0), assigned(6,7), assigned(7,1), assigned(7,2), assigned(7,8), assigned(8,2), assigned(8,6), insquare(0,0,0), insquare(0,0,1), insquare(0,0,2), insquare(0,1,0), insquare(0,1,1), insquare(0,1,2), insquare(0,2,0), insquare(0,2,1), insquare(0,2,2), insquare(1,3,0), insquare(1,3,1), insquare(1,3,2), insquare(1,4,0), insquare(1,4,1), insquare(1,4,2), insquare(1,5,0), insquare(1,5,1), insquare(1,5,2), insquare(2,6,0), insquare(2,6,1), insquare(2,6,2), insquare(2,7,0), insquare(2,7,1), insquare(2,7,2), insquare(2,8,0), insquare(2,8,1), insquare(2,8,2), insquare(3,0,3), insquare(3,0,4), insquare(3,0,5), insquare(3,1,3), insquare(3,1,4), insquare(3,1,5), insquare(3,2,3), insquare(3,2,4), insquare(3,2,5), insquare(4,3,3), insquare(4,3,4), insquare(4,3,5), insquare(4,4,3), insquare(4,4,4), insquare(4,4,5), insquare(4,5,3), insquare(4,5,4), insquare(4,5,5), insquare(5,6,3), insquare(5,6,4), insquare(5,6,5), insquare(5,7,3), insquare(5,7,4), insquare(5,7,5), insquare(5,8,3), insquare(5,8,4), insquare(5,8,5), insquare(6,0,6), insquare(6,0,7), insquare(6,0,8), insquare(6,1,6), insquare(6,1,7), insquare(6,1,8), insquare(6,2,6), insquare(6,2,7), insquare(6,2,8), insquare(7,3,6), insquare(7,3,7), insquare(7,3,8), insquare(7,4,6), insquare(7,4,7), insquare(7,4,8), insquare(7,5,6), insquare(7,5,7), insquare(7,5,8), insquare(8,6,6), insquare(8,6,7), insquare(8,6,8), insquare(8,7,6), insquare(8,7,7), insquare(8,7,8), insquare(8,8,6), insquare(8,8,7), insquare(8,8,8), div(0,1,0), div(0,2,0), div(0,3,0), div(0,4,0), div(0,5,0), div(0,6,0), div(0,7,0), div(0,8,0), div(1,1,1), div(1,2,0), div(1,3,0), div(1,4,0), div(1,5,0), div(1,6,0), div(1,7,0), div(1,8,0), div(2,1,2), div(2,2,1), div(2,3,0), div(2,4,0), div(2,5,0), div(2,6,0), div(2,7,0), div(2,8,0), div(3,1,3), div(3,2,1), div(3,3,1), div(3,4,0), div(3,5,0), div(3,6,0), div(3,7,0), div(3,8,0), div(4,1,4), div(4,2,2), div(4,3,1), div(4,4,1), div(4,5,0), div(4,6,0), div(4,7,0), div(4,8,0), div(5,1,5), div(5,2,2), div(5,3,1), div(5,4,1), div(5,5,1), div(5,6,0), div(5,7,0), div(5,8,0), div(6,1,6), div(6,2,3), div(6,3,2), div(6,4,1), div(6,5,1), div(6,6,1), div(6,7,0), div(6,8,0), div(7,1,7), div(7,2,3), div(7,3,2), div(7,4,1), div(7,5,1), div(7,6,1), div(7,7,1), div(7,8,0), div(8,1,8), div(8,2,4), div(8,3,2), div(8,4,2), div(8,5,1), div(8,6,1), div(8,7,1), div(8,8,1), samesquare(0,0,0,0), samesquare(0,0,0,1), samesquare(0,0,0,2), samesquare(0,0,1,0), samesquare(0,0,1,1), samesquare(0,0,1,2), samesquare(0,0,2,0), samesquare(0,0,2,1), samesquare(0,0,2,2), samesquare(0,1,0,0), samesquare(0,1,0,1), samesquare(0,1,0,2), samesquare(0,1,1,0), samesquare(0,1,1,1), samesquare(0,1,1,2), samesquare(0,1,2,0), samesquare(0,1,2,1), samesquare(0,1,2,2), samesquare(0,2,0,0), samesquare(0,2,0,1), samesquare(0,2,0,2), samesquare(0,2,1,0), samesquare(0,2,1,1), samesquare(0,2,1,2), samesquare(0,2,2,0), samesquare(0,2,2,1), samesquare(0,2,2,2), samesquare(0,3,0,3), samesquare(0,3,0,4), samesquare(0,3,0,5), samesquare(0,3,1,3), samesquare(0,3,1,4), samesquare(0,3,1,5), samesquare(0,3,2,3), samesquare(0,3,2,4), samesquare(0,3,2,5), samesquare(0,4,0,3), samesquare(0,4,0,4), samesquare(0,4,0,5), samesquare(0,4,1,3), samesquare(0,4,1,4), samesquare(0,4,1,5), samesquare(0,4,2,3), samesquare(0,4,2,4), samesquare(0,4,2,5), samesquare(0,5,0,3), samesquare(0,5,0,4), samesquare(0,5,0,5), samesquare(0,5,1,3), samesquare(0,5,1,4), samesquare(0,5,1,5), samesquare(0,5,2,3), samesquare(0,5,2,4), samesquare(0,5,2,5), samesquare(0,6,0,6), samesquare(0,6,0,7), samesquare(0,6,0,8), samesquare(0,6,1,6), samesquare(0,6,1,7), samesquare(0,6,1,8), samesquare(0,6,2,6), samesquare(0,6,2,7), samesquare(0,6,2,8), samesquare(0,7,0,6), samesquare(0,7,0,7), samesquare(0,7,0,8), samesquare(0,7,1,6), samesquare(0,7,1,7), samesquare(0,7,1,8), samesquare(0,7,2,6), samesquare(0,7,2,7), samesquare(0,7,2,8), samesquare(0,8,0,6), samesquare(0,8,0,7), samesquare(0,8,0,8), samesquare(0,8,1,6), samesquare(0,8,1,7), samesquare(0,8,1,8), samesquare(0,8,2,6), samesquare(0,8,2,7), samesquare(0,8,2,8), samesquare(1,0,0,0), samesquare(1,0,0,1), samesquare(1,0,0,2), samesquare(1,0,1,0), samesquare(1,0,1,1), samesquare(1,0,1,2), samesquare(1,0,2,0), samesquare(1,0,2,1), samesquare(1,0,2,2), samesquare(1,1,0,0), samesquare(1,1,0,1), samesquare(1,1,0,2), samesquare(1,1,1,0), samesquare(1,1,1,1), samesquare(1,1,1,2), samesquare(1,1,2,0), samesquare(1,1,2,1), samesquare(1,1,2,2), samesquare(1,2,0,0), samesquare(1,2,0,1), samesquare(1,2,0,2), samesquare(1,2,1,0), samesquare(1,2,1,1), samesquare(1,2,1,2), samesquare(1,2,2,0), samesquare(1,2,2,1), samesquare(1,2,2,2), samesquare(1,3,0,3), samesquare(1,3,0,4), samesquare(1,3,0,5), samesquare(1,3,1,3), samesquare(1,3,1,4), samesquare(1,3,1,5), samesquare(1,3,2,3), samesquare(1,3,2,4), samesquare(1,3,2,5), samesquare(1,4,0,3), samesquare(1,4,0,4), samesquare(1,4,0,5), samesquare(1,4,1,3), samesquare(1,4,1,4), samesquare(1,4,1,5), samesquare(1,4,2,3), samesquare(1,4,2,4), samesquare(1,4,2,5), samesquare(1,5,0,3), samesquare(1,5,0,4), samesquare(1,5,0,5), samesquare(1,5,1,3), samesquare(1,5,1,4), samesquare(1,5,1,5), samesquare(1,5,2,3), samesquare(1,5,2,4), samesquare(1,5,2,5), samesquare(1,6,0,6), samesquare(1,6,0,7), samesquare(1,6,0,8), samesquare(1,6,1,6), samesquare(1,6,1,7), samesquare(1,6,1,8), samesquare(1,6,2,6), samesquare(1,6,2,7), samesquare(1,6,2,8), samesquare(1,7,0,6), samesquare(1,7,0,7), samesquare(1,7,0,8), samesquare(1,7,1,6), samesquare(1,7,1,7), samesquare(1,7,1,8), samesquare(1,7,2,6), samesquare(1,7,2,7), samesquare(1,7,2,8), samesquare(1,8,0,6), samesquare(1,8,0,7), samesquare(1,8,0,8), samesquare(1,8,1,6), samesquare(1,8,1,7), samesquare(1,8,1,8), samesquare(1,8,2,6), samesquare(1,8,2,7), samesquare(1,8,2,8), samesquare(2,0,0,0), samesquare(2,0,0,1), samesquare(2,0,0,2), samesquare(2,0,1,0), samesquare(2,0,1,1), samesquare(2,0,1,2), samesquare(2,0,2,0), samesquare(2,0,2,1), samesquare(2,0,2,2), samesquare(2,1,0,0), samesquare(2,1,0,1), samesquare(2,1,0,2), samesquare(2,1,1,0), samesquare(2,1,1,1), samesquare(2,1,1,2), samesquare(2,1,2,0), samesquare(2,1,2,1), samesquare(2,1,2,2), samesquare(2,2,0,0), samesquare(2,2,0,1), samesquare(2,2,0,2), samesquare(2,2,1,0), samesquare(2,2,1,1), samesquare(2,2,1,2), samesquare(2,2,2,0), samesquare(2,2,2,1), samesquare(2,2,2,2), samesquare(2,3,0,3), samesquare(2,3,0,4), samesquare(2,3,0,5), samesquare(2,3,1,3), samesquare(2,3,1,4), samesquare(2,3,1,5), samesquare(2,3,2,3), samesquare(2,3,2,4), samesquare(2,3,2,5), samesquare(2,4,0,3), samesquare(2,4,0,4), samesquare(2,4,0,5), samesquare(2,4,1,3), samesquare(2,4,1,4), samesquare(2,4,1,5), samesquare(2,4,2,3), samesquare(2,4,2,4), samesquare(2,4,2,5), samesquare(2,5,0,3), samesquare(2,5,0,4), samesquare(2,5,0,5), samesquare(2,5,1,3), samesquare(2,5,1,4), samesquare(2,5,1,5), samesquare(2,5,2,3), samesquare(2,5,2,4), samesquare(2,5,2,5), samesquare(2,6,0,6), samesquare(2,6,0,7), samesquare(2,6,0,8), samesquare(2,6,1,6), samesquare(2,6,1,7), samesquare(2,6,1,8), samesquare(2,6,2,6), samesquare(2,6,2,7), samesquare(2,6,2,8), samesquare(2,7,0,6), samesquare(2,7,0,7), samesquare(2,7,0,8), samesquare(2,7,1,6), samesquare(2,7,1,7), samesquare(2,7,1,8), samesquare(2,7,2,6), samesquare(2,7,2,7), samesquare(2,7,2,8), samesquare(2,8,0,6), samesquare(2,8,0,7), samesquare(2,8,0,8), samesquare(2,8,1,6), samesquare(2,8,1,7), samesquare(2,8,1,8), samesquare(2,8,2,6), samesquare(2,8,2,7), samesquare(2,8,2,8), samesquare(3,0,3,0), samesquare(3,0,3,1), samesquare(3,0,3,2), samesquare(3,0,4,0), samesquare(3,0,4,1), samesquare(3,0,4,2), samesquare(3,0,5,0), samesquare(3,0,5,1), samesquare(3,0,5,2), samesquare(3,1,3,0), samesquare(3,1,3,1), samesquare(3,1,3,2), samesquare(3,1,4,0), samesquare(3,1,4,1), samesquare(3,1,4,2), samesquare(3,1,5,0), samesquare(3,1,5,1), samesquare(3,1,5,2), samesquare(3,2,3,0), samesquare(3,2,3,1), samesquare(3,2,3,2), samesquare(3,2,4,0), samesquare(3,2,4,1), samesquare(3,2,4,2), samesquare(3,2,5,0), samesquare(3,2,5,1), samesquare(3,2,5,2), samesquare(3,3,3,3), samesquare(3,3,3,4), samesquare(3,3,3,5), samesquare(3,3,4,3), samesquare(3,3,4,4), samesquare(3,3,4,5), samesquare(3,3,5,3), samesquare(3,3,5,4), samesquare(3,3,5,5), samesquare(3,4,3,3), samesquare(3,4,3,4), samesquare(3,4,3,5), samesquare(3,4,4,3), samesquare(3,4,4,4), samesquare(3,4,4,5), samesquare(3,4,5,3), samesquare(3,4,5,4), samesquare(3,4,5,5), samesquare(3,5,3,3), samesquare(3,5,3,4), samesquare(3,5,3,5), samesquare(3,5,4,3), samesquare(3,5,4,4), samesquare(3,5,4,5), samesquare(3,5,5,3), samesquare(3,5,5,4), samesquare(3,5,5,5), samesquare(3,6,3,6), samesquare(3,6,3,7), samesquare(3,6,3,8), samesquare(3,6,4,6), samesquare(3,6,4,7), samesquare(3,6,4,8), samesquare(3,6,5,6), samesquare(3,6,5,7), samesquare(3,6,5,8), samesquare(3,7,3,6), samesquare(3,7,3,7), samesquare(3,7,3,8), samesquare(3,7,4,6), samesquare(3,7,4,7), samesquare(3,7,4,8), samesquare(3,7,5,6), samesquare(3,7,5,7), samesquare(3,7,5,8), samesquare(3,8,3,6), samesquare(3,8,3,7), samesquare(3,8,3,8), samesquare(3,8,4,6), samesquare(3,8,4,7), samesquare(3,8,4,8), samesquare(3,8,5,6), samesquare(3,8,5,7), samesquare(3,8,5,8), samesquare(4,0,3,0), samesquare(4,0,3,1), samesquare(4,0,3,2), samesquare(4,0,4,0), samesquare(4,0,4,1), samesquare(4,0,4,2), samesquare(4,0,5,0), samesquare(4,0,5,1), samesquare(4,0,5,2), samesquare(4,1,3,0), samesquare(4,1,3,1), samesquare(4,1,3,2), samesquare(4,1,4,0), samesquare(4,1,4,1), samesquare(4,1,4,2), samesquare(4,1,5,0), samesquare(4,1,5,1), samesquare(4,1,5,2), samesquare(4,2,3,0), samesquare(4,2,3,1), samesquare(4,2,3,2), samesquare(4,2,4,0), samesquare(4,2,4,1), samesquare(4,2,4,2), samesquare(4,2,5,0), samesquare(4,2,5,1), samesquare(4,2,5,2), samesquare(4,3,3,3), samesquare(4,3,3,4), samesquare(4,3,3,5), samesquare(4,3,4,3), samesquare(4,3,4,4), samesquare(4,3,4,5), samesquare(4,3,5,3), samesquare(4,3,5,4), samesquare(4,3,5,5), samesquare(4,4,3,3), samesquare(4,4,3,4), samesquare(4,4,3,5), samesquare(4,4,4,3), samesquare(4,4,4,4), samesquare(4,4,4,5), samesquare(4,4,5,3), samesquare(4,4,5,4), samesquare(4,4,5,5), samesquare(4,5,3,3), samesquare(4,5,3,4), samesquare(4,5,3,5), samesquare(4,5,4,3), samesquare(4,5,4,4), samesquare(4,5,4,5), samesquare(4,5,5,3), samesquare(4,5,5,4), samesquare(4,5,5,5), samesquare(4,6,3,6), samesquare(4,6,3,7), samesquare(4,6,3,8), samesquare(4,6,4,6), samesquare(4,6,4,7), samesquare(4,6,4,8), samesquare(4,6,5,6), samesquare(4,6,5,7), samesquare(4,6,5,8), samesquare(4,7,3,6), samesquare(4,7,3,7), samesquare(4,7,3,8), samesquare(4,7,4,6), samesquare(4,7,4,7), samesquare(4,7,4,8), samesquare(4,7,5,6), samesquare(4,7,5,7), samesquare(4,7,5,8), samesquare(4,8,3,6), samesquare(4,8,3,7), samesquare(4,8,3,8), samesquare(4,8,4,6), samesquare(4,8,4,7), samesquare(4,8,4,8), samesquare(4,8,5,6), samesquare(4,8,5,7), samesquare(4,8,5,8), samesquare(5,0,3,0), samesquare(5,0,3,1), samesquare(5,0,3,2), samesquare(5,0,4,0), samesquare(5,0,4,1), samesquare(5,0,4,2), samesquare(5,0,5,0), samesquare(5,0,5,1), samesquare(5,0,5,2), samesquare(5,1,3,0), samesquare(5,1,3,1), samesquare(5,1,3,2), samesquare(5,1,4,0), samesquare(5,1,4,1), samesquare(5,1,4,2), samesquare(5,1,5,0), samesquare(5,1,5,1), samesquare(5,1,5,2), samesquare(5,2,3,0), samesquare(5,2,3,1), samesquare(5,2,3,2), samesquare(5,2,4,0), samesquare(5,2,4,1), samesquare(5,2,4,2), samesquare(5,2,5,0), samesquare(5,2,5,1), samesquare(5,2,5,2), samesquare(5,3,3,3), samesquare(5,3,3,4), samesquare(5,3,3,5), samesquare(5,3,4,3), samesquare(5,3,4,4), samesquare(5,3,4,5), samesquare(5,3,5,3), samesquare(5,3,5,4), samesquare(5,3,5,5), samesquare(5,4,3,3), samesquare(5,4,3,4), samesquare(5,4,3,5), samesquare(5,4,4,3), samesquare(5,4,4,4), samesquare(5,4,4,5), samesquare(5,4,5,3), samesquare(5,4,5,4), samesquare(5,4,5,5), samesquare(5,5,3,3), samesquare(5,5,3,4), samesquare(5,5,3,5), samesquare(5,5,4,3), samesquare(5,5,4,4), samesquare(5,5,4,5), samesquare(5,5,5,3), samesquare(5,5,5,4), samesquare(5,5,5,5), samesquare(5,6,3,6), samesquare(5,6,3,7), samesquare(5,6,3,8), samesquare(5,6,4,6), samesquare(5,6,4,7), samesquare(5,6,4,8), samesquare(5,6,5,6), samesquare(5,6,5,7), samesquare(5,6,5,8), samesquare(5,7,3,6), samesquare(5,7,3,7), samesquare(5,7,3,8), samesquare(5,7,4,6), samesquare(5,7,4,7), samesquare(5,7,4,8), samesquare(5,7,5,6), samesquare(5,7,5,7), samesquare(5,7,5,8), samesquare(5,8,3,6), samesquare(5,8,3,7), samesquare(5,8,3,8), samesquare(5,8,4,6), samesquare(5,8,4,7), samesquare(5,8,4,8), samesquare(5,8,5,6), samesquare(5,8,5,7), samesquare(5,8,5,8), samesquare(6,0,6,0), samesquare(6,0,6,1), samesquare(6,0,6,2), samesquare(6,0,7,0), samesquare(6,0,7,1), samesquare(6,0,7,2), samesquare(6,0,8,0), samesquare(6,0,8,1), samesquare(6,0,8,2), samesquare(6,1,6,0), samesquare(6,1,6,1), samesquare(6,1,6,2), samesquare(6,1,7,0), samesquare(6,1,7,1), samesquare(6,1,7,2), samesquare(6,1,8,0), samesquare(6,1,8,1), samesquare(6,1,8,2), samesquare(6,2,6,0), samesquare(6,2,6,1), samesquare(6,2,6,2), samesquare(6,2,7,0), samesquare(6,2,7,1), samesquare(6,2,7,2), samesquare(6,2,8,0), samesquare(6,2,8,1), samesquare(6,2,8,2), samesquare(6,3,6,3), samesquare(6,3,6,4), samesquare(6,3,6,5), samesquare(6,3,7,3), samesquare(6,3,7,4), samesquare(6,3,7,5), samesquare(6,3,8,3), samesquare(6,3,8,4), samesquare(6,3,8,5), samesquare(6,4,6,3), samesquare(6,4,6,4), samesquare(6,4,6,5), samesquare(6,4,7,3), samesquare(6,4,7,4), samesquare(6,4,7,5), samesquare(6,4,8,3), samesquare(6,4,8,4), samesquare(6,4,8,5), samesquare(6,5,6,3), samesquare(6,5,6,4), samesquare(6,5,6,5), samesquare(6,5,7,3), samesquare(6,5,7,4), samesquare(6,5,7,5), samesquare(6,5,8,3), samesquare(6,5,8,4), samesquare(6,5,8,5), samesquare(6,6,6,6), samesquare(6,6,6,7), samesquare(6,6,6,8), samesquare(6,6,7,6), samesquare(6,6,7,7), samesquare(6,6,7,8), samesquare(6,6,8,6), samesquare(6,6,8,7), samesquare(6,6,8,8), samesquare(6,7,6,6), samesquare(6,7,6,7), samesquare(6,7,6,8), samesquare(6,7,7,6), samesquare(6,7,7,7), samesquare(6,7,7,8), samesquare(6,7,8,6), samesquare(6,7,8,7), samesquare(6,7,8,8), samesquare(6,8,6,6), samesquare(6,8,6,7), samesquare(6,8,6,8), samesquare(6,8,7,6), samesquare(6,8,7,7), samesquare(6,8,7,8), samesquare(6,8,8,6), samesquare(6,8,8,7), samesquare(6,8,8,8), samesquare(7,0,6,0), samesquare(7,0,6,1), samesquare(7,0,6,2), samesquare(7,0,7,0), samesquare(7,0,7,1), samesquare(7,0,7,2), samesquare(7,0,8,0), samesquare(7,0,8,1), samesquare(7,0,8,2), samesquare(7,1,6,0), samesquare(7,1,6,1), samesquare(7,1,6,2), samesquare(7,1,7,0), samesquare(7,1,7,1), samesquare(7,1,7,2), samesquare(7,1,8,0), samesquare(7,1,8,1), samesquare(7,1,8,2), samesquare(7,2,6,0), samesquare(7,2,6,1), samesquare(7,2,6,2), samesquare(7,2,7,0), samesquare(7,2,7,1), samesquare(7,2,7,2), samesquare(7,2,8,0), samesquare(7,2,8,1), samesquare(7,2,8,2), samesquare(7,3,6,3), samesquare(7,3,6,4), samesquare(7,3,6,5), samesquare(7,3,7,3), samesquare(7,3,7,4), samesquare(7,3,7,5), samesquare(7,3,8,3), samesquare(7,3,8,4), samesquare(7,3,8,5), samesquare(7,4,6,3), samesquare(7,4,6,4), samesquare(7,4,6,5), samesquare(7,4,7,3), samesquare(7,4,7,4), samesquare(7,4,7,5), samesquare(7,4,8,3), samesquare(7,4,8,4), samesquare(7,4,8,5), samesquare(7,5,6,3), samesquare(7,5,6,4), samesquare(7,5,6,5), samesquare(7,5,7,3), samesquare(7,5,7,4), samesquare(7,5,7,5), samesquare(7,5,8,3), samesquare(7,5,8,4), samesquare(7,5,8,5), samesquare(7,6,6,6), samesquare(7,6,6,7), samesquare(7,6,6,8), samesquare(7,6,7,6), samesquare(7,6,7,7), samesquare(7,6,7,8), samesquare(7,6,8,6), samesquare(7,6,8,7), samesquare(7,6,8,8), samesquare(7,7,6,6), samesquare(7,7,6,7), samesquare(7,7,6,8), samesquare(7,7,7,6), samesquare(7,7,7,7), samesquare(7,7,7,8), samesquare(7,7,8,6), samesquare(7,7,8,7), samesquare(7,7,8,8), samesquare(7,8,6,6), samesquare(7,8,6,7), samesquare(7,8,6,8), samesquare(7,8,7,6), samesquare(7,8,7,7), samesquare(7,8,7,8), samesquare(7,8,8,6), samesquare(7,8,8,7), samesquare(7,8,8,8), samesquare(8,0,6,0), samesquare(8,0,6,1), samesquare(8,0,6,2), samesquare(8,0,7,0), samesquare(8,0,7,1), samesquare(8,0,7,2), samesquare(8,0,8,0), samesquare(8,0,8,1), samesquare(8,0,8,2), samesquare(8,1,6,0), samesquare(8,1,6,1), samesquare(8,1,6,2), samesquare(8,1,7,0), samesquare(8,1,7,1), samesquare(8,1,7,2), samesquare(8,1,8,0), samesquare(8,1,8,1), samesquare(8,1,8,2), samesquare(8,2,6,0), samesquare(8,2,6,1), samesquare(8,2,6,2), samesquare(8,2,7,0), samesquare(8,2,7,1), samesquare(8,2,7,2), samesquare(8,2,8,0), samesquare(8,2,8,1), samesquare(8,2,8,2), samesquare(8,3,6,3), samesquare(8,3,6,4), samesquare(8,3,6,5), samesquare(8,3,7,3), samesquare(8,3,7,4), samesquare(8,3,7,5), samesquare(8,3,8,3), samesquare(8,3,8,4), samesquare(8,3,8,5), samesquare(8,4,6,3), samesquare(8,4,6,4), samesquare(8,4,6,5), samesquare(8,4,7,3), samesquare(8,4,7,4), samesquare(8,4,7,5), samesquare(8,4,8,3), samesquare(8,4,8,4), samesquare(8,4,8,5), samesquare(8,5,6,3), samesquare(8,5,6,4), samesquare(8,5,6,5), samesquare(8,5,7,3), samesquare(8,5,7,4), samesquare(8,5,7,5), samesquare(8,5,8,3), samesquare(8,5,8,4), samesquare(8,5,8,5), samesquare(8,6,6,6), samesquare(8,6,6,7), samesquare(8,6,6,8), samesquare(8,6,7,6), samesquare(8,6,7,7), samesquare(8,6,7,8), samesquare(8,6,8,6), samesquare(8,6,8,7), samesquare(8,6,8,8), samesquare(8,7,6,6), samesquare(8,7,6,7), samesquare(8,7,6,8), samesquare(8,7,7,6), samesquare(8,7,7,7), samesquare(8,7,7,8), samesquare(8,7,8,6), samesquare(8,7,8,7), samesquare(8,7,8,8), samesquare(8,8,6,6), samesquare(8,8,6,7), samesquare(8,8,6,8), samesquare(8,8,7,6), samesquare(8,8,7,7), samesquare(8,8,7,8), samesquare(8,8,8,6), samesquare(8,8,8,7), samesquare(8,8,8,8), nocell(1,0,1), nocell(2,0,1), nocell(3,0,1), nocell(4,0,1), nocell(5,0,1), nocell(6,0,1), nocell(7,0,1), nocell(8,0,1), nocell(0,1,1), nocell(1,1,1), nocell(2,1,1), nocell(3,1,1), nocell(5,1,1), nocell(6,1,1), nocell(7,1,1), nocell(8,1,1), nocell(0,2,1), nocell(1,2,1), nocell(2,2,1), nocell(3,2,1), nocell(4,2,1), nocell(5,2,1), nocell(6,2,1), nocell(8,2,1), nocell(0,3,1), cell(1,3,1), nocell(2,3,1), nocell(3,3,1), nocell(4,3,1), nocell(5,3,1), nocell(6,3,1), nocell(7,3,1), nocell(8,3,1), nocell(0,4,1), nocell(1,4,1), nocell(2,4,1), cell(3,4,1), nocell(4,4,1), nocell(5,4,1), nocell(6,4,1), nocell(7,4,1), nocell(8,4,1), nocell(0,5,1), nocell(1,5,1), nocell(2,5,1), nocell(3,5,1), nocell(4,5,1), nocell(5,5,1), nocell(6,5,1), nocell(7,5,1), cell(8,5,1), nocell(0,6,1), nocell(1,6,1), nocell(2,6,1), nocell(3,6,1), nocell(4,6,1), cell(5,6,1), nocell(6,6,1), nocell(7,6,1), nocell(8,6,1), nocell(0,7,1), nocell(1,7,1), nocell(2,7,1), nocell(3,7,1), nocell(4,7,1), nocell(5,7,1), nocell(7,7,1), nocell(8,7,1), nocell(0,8,1), nocell(1,8,1), cell(2,8,1), nocell(3,8,1), nocell(4,8,1), nocell(5,8,1), nocell(6,8,1), nocell(7,8,1), nocell(8,8,1), nocell(0,0,2), nocell(1,0,2), nocell(2,0,2), nocell(3,0,2), nocell(4,0,2), nocell(5,0,2), nocell(6,0,2), cell(7,0,2), nocell(8,0,2), nocell(0,1,2), nocell(1,1,2), nocell(2,1,2), nocell(3,1,2), nocell(4,1,2), cell(5,1,2), nocell(6,1,2), nocell(7,1,2), nocell(8,1,2), cell(0,2,2), nocell(1,2,2), nocell(2,2,2), nocell(3,2,2), nocell(4,2,2), nocell(5,2,2), nocell(6,2,2), nocell(7,2,2), nocell(8,2,2), nocell(0,3,2), nocell(1,3,2), nocell(2,3,2), nocell(3,3,2), nocell(4,3,2), nocell(5,3,2), nocell(6,3,2), nocell(7,3,2), cell(8,3,2), nocell(0,4,2), nocell(2,4,2), nocell(3,4,2), nocell(4,4,2), nocell(5,4,2), nocell(6,4,2), nocell(7,4,2), nocell(8,4,2), nocell(0,5,2), nocell(1,5,2), nocell(2,5,2), cell(3,5,2), nocell(4,5,2), nocell(5,5,2), nocell(6,5,2), nocell(7,5,2), nocell(8,5,2), nocell(0,6,2), nocell(1,6,2), nocell(2,6,2), nocell(3,6,2), nocell(4,6,2), nocell(5,6,2), cell(6,6,2), nocell(7,6,2), nocell(8,6,2), nocell(0,7,2), nocell(1,7,2), cell(2,7,2), nocell(3,7,2), nocell(4,7,2), nocell(5,7,2), nocell(6,7,2), nocell(7,7,2), nocell(8,7,2), nocell(0,8,2), nocell(1,8,2), nocell(2,8,2), nocell(3,8,2), nocell(5,8,2), nocell(6,8,2), nocell(7,8,2), nocell(8,8,2), nocell(0,0,3), nocell(1,0,3), nocell(2,0,3), nocell(3,0,3), nocell(4,0,3), nocell(5,0,3), nocell(7,0,3), nocell(8,0,3), nocell(0,1,3), nocell(2,1,3), nocell(3,1,3), nocell(4,1,3), nocell(5,1,3), nocell(6,1,3), nocell(7,1,3), nocell(8,1,3), nocell(0,2,3), nocell(1,2,3), nocell(2,2,3), nocell(3,2,3), cell(4,2,3), nocell(5,2,3), nocell(6,2,3), nocell(7,2,3), nocell(8,2,3), nocell(0,3,3), nocell(1,3,3), nocell(2,3,3), nocell(4,3,3), nocell(5,3,3), nocell(6,3,3), nocell(7,3,3), nocell(8,3,3), nocell(0,4,3), nocell(1,4,3), nocell(2,4,3), nocell(3,4,3), nocell(4,4,3), nocell(5,4,3), nocell(6,4,3), cell(7,4,3), nocell(8,4,3), nocell(0,5,3), nocell(1,5,3), cell(2,5,3), nocell(3,5,3), nocell(4,5,3), nocell(5,5,3), nocell(6,5,3), nocell(7,5,3), nocell(8,5,3), nocell(0,6,3), nocell(1,6,3), nocell(2,6,3), nocell(3,6,3), nocell(4,6,3), nocell(5,6,3), nocell(6,6,3), nocell(7,6,3), nocell(0,7,3), nocell(1,7,3), nocell(2,7,3), nocell(3,7,3), nocell(4,7,3), cell(5,7,3), nocell(6,7,3), nocell(7,7,3), nocell(8,7,3), cell(0,8,3), nocell(1,8,3), nocell(2,8,3), nocell(3,8,3), nocell(4,8,3), nocell(5,8,3), nocell(6,8,3), nocell(7,8,3), nocell(8,8,3), nocell(0,0,4), nocell(1,0,4), nocell(2,0,4), cell(3,0,4), nocell(4,0,4), nocell(5,0,4), nocell(6,0,4), nocell(7,0,4), nocell(8,0,4), nocell(0,1,4), nocell(1,1,4), nocell(2,1,4), nocell(3,1,4), nocell(4,1,4), nocell(5,1,4), nocell(6,1,4), nocell(8,1,4), nocell(0,2,4), cell(1,2,4), nocell(2,2,4), nocell(3,2,4), nocell(4,2,4), nocell(5,2,4), nocell(6,2,4), nocell(7,2,4), nocell(8,2,4), nocell(0,3,4), nocell(1,3,4), nocell(2,3,4), nocell(3,3,4), nocell(4,3,4), nocell(5,3,4), cell(6,3,4), nocell(7,3,4), nocell(8,3,4), nocell(0,4,4), nocell(1,4,4), cell(2,4,4), nocell(3,4,4), nocell(4,4,4), nocell(5,4,4), nocell(6,4,4), nocell(7,4,4), nocell(8,4,4), nocell(0,5,4), nocell(1,5,4), nocell(2,5,4), nocell(3,5,4), nocell(4,5,4), nocell(6,5,4), nocell(7,5,4), nocell(8,5,4), cell(0,6,4), nocell(1,6,4), nocell(2,6,4), nocell(3,6,4), nocell(4,6,4), nocell(5,6,4), nocell(6,6,4), nocell(7,6,4), nocell(8,6,4), nocell(0,7,4), nocell(1,7,4), nocell(2,7,4), nocell(3,7,4), cell(4,7,4), nocell(5,7,4), nocell(6,7,4), nocell(7,7,4), nocell(8,7,4), nocell(0,8,4), nocell(1,8,4), nocell(2,8,4), nocell(3,8,4), nocell(4,8,4), nocell(5,8,4), nocell(6,8,4), nocell(7,8,4), cell(8,8,4), nocell(0,0,5), cell(1,0,5), nocell(2,0,5), nocell(3,0,5), nocell(4,0,5), nocell(5,0,5), nocell(6,0,5), nocell(7,0,5), nocell(8,0,5), nocell(0,1,5), nocell(1,1,5), nocell(2,1,5), nocell(3,1,5), nocell(4,1,5), nocell(5,1,5), cell(6,1,5), nocell(7,1,5), nocell(8,1,5), nocell(0,2,5), nocell(1,2,5), nocell(2,2,5), nocell(4,2,5), nocell(5,2,5), nocell(6,2,5), nocell(7,2,5), nocell(8,2,5), nocell(0,3,5), nocell(1,3,5), nocell(2,3,5), nocell(3,3,5), cell(4,3,5), nocell(5,3,5), nocell(6,3,5), nocell(7,3,5), nocell(8,3,5), cell(0,4,5), nocell(1,4,5), nocell(2,4,5), nocell(3,4,5), nocell(4,4,5), nocell(5,4,5), nocell(6,4,5), nocell(7,4,5), nocell(8,4,5), nocell(0,5,5), nocell(1,5,5), nocell(2,5,5), nocell(3,5,5), nocell(4,5,5), nocell(5,5,5), nocell(6,5,5), cell(7,5,5), nocell(8,5,5), nocell(0,6,5), nocell(1,6,5), nocell(3,6,5), nocell(4,6,5), nocell(5,6,5), nocell(6,6,5), nocell(7,6,5), nocell(8,6,5), nocell(0,7,5), nocell(1,7,5), nocell(2,7,5), nocell(3,7,5), nocell(4,7,5), nocell(5,7,5), nocell(6,7,5), nocell(7,7,5), cell(8,7,5), nocell(0,8,5), nocell(1,8,5), nocell(2,8,5), nocell(3,8,5), nocell(4,8,5), cell(5,8,5), nocell(6,8,5), nocell(7,8,5), nocell(8,8,5), nocell(0,0,6), nocell(1,0,6), nocell(2,0,6), nocell(3,0,6), nocell(4,0,6), nocell(6,0,6), nocell(7,0,6), nocell(8,0,6), cell(0,1,6), nocell(1,1,6), nocell(2,1,6), nocell(3,1,6), nocell(4,1,6), nocell(5,1,6), nocell(6,1,6), nocell(7,1,6), nocell(8,1,6), nocell(0,2,6), nocell(1,2,6), nocell(2,2,6), nocell(3,2,6), nocell(4,2,6), nocell(5,2,6), cell(6,2,6), nocell(7,2,6), nocell(8,2,6), nocell(0,3,6), nocell(1,3,6), nocell(3,3,6), nocell(4,3,6), nocell(5,3,6), nocell(6,3,6), nocell(7,3,6), nocell(8,3,6), nocell(0,4,6), nocell(1,4,6), nocell(2,4,6), nocell(3,4,6), nocell(4,4,6), nocell(5,4,6), nocell(6,4,6), nocell(7,4,6), cell(8,4,6), nocell(0,5,6), nocell(1,5,6), nocell(2,5,6), nocell(3,5,6), cell(4,5,6), nocell(5,5,6), nocell(6,5,6), nocell(7,5,6), nocell(8,5,6), nocell(0,6,6), cell(1,6,6), nocell(2,6,6), nocell(3,6,6), nocell(4,6,6), nocell(5,6,6), nocell(6,6,6), nocell(7,6,6), nocell(8,6,6), nocell(0,7,6), nocell(1,7,6), nocell(2,7,6), nocell(3,7,6), nocell(4,7,6), nocell(5,7,6), nocell(6,7,6), cell(7,7,6), nocell(8,7,6), nocell(0,8,6), nocell(1,8,6), nocell(2,8,6), cell(3,8,6), nocell(4,8,6), nocell(5,8,6), nocell(6,8,6), nocell(7,8,6), nocell(8,8,6), nocell(0,0,7), nocell(1,0,7), cell(2,0,7), nocell(3,0,7), nocell(4,0,7), nocell(5,0,7), nocell(6,0,7), nocell(7,0,7), nocell(8,0,7), nocell(0,1,7), nocell(1,1,7), nocell(2,1,7), cell(3,1,7), nocell(4,1,7), nocell(5,1,7), nocell(6,1,7), nocell(7,1,7), nocell(8,1,7), nocell(0,2,7), nocell(1,2,7), nocell(2,2,7), nocell(3,2,7), nocell(4,2,7), nocell(5,2,7), nocell(6,2,7), nocell(7,2,7), nocell(0,3,7), nocell(1,3,7), nocell(2,3,7), nocell(3,3,7), nocell(4,3,7), cell(5,3,7), nocell(6,3,7), nocell(7,3,7), nocell(8,3,7), nocell(0,4,7), nocell(1,4,7), nocell(2,4,7), nocell(3,4,7), nocell(4,4,7), nocell(5,4,7), cell(6,4,7), nocell(7,4,7), nocell(8,4,7), nocell(1,5,7), nocell(2,5,7), nocell(3,5,7), nocell(4,5,7), nocell(5,5,7), nocell(6,5,7), nocell(7,5,7), nocell(8,5,7), nocell(0,6,7), nocell(1,6,7), nocell(2,6,7), nocell(3,6,7), cell(4,6,7), nocell(5,6,7), nocell(6,6,7), nocell(7,6,7), nocell(8,6,7), nocell(0,7,7), cell(1,7,7), nocell(2,7,7), nocell(3,7,7), nocell(4,7,7), nocell(5,7,7), nocell(6,7,7), nocell(7,7,7), nocell(8,7,7), nocell(0,8,7), nocell(1,8,7), nocell(2,8,7), nocell(3,8,7), nocell(4,8,7), nocell(5,8,7), nocell(6,8,7), nocell(8,8,7), nocell(0,0,8), nocell(1,0,8), nocell(2,0,8), nocell(3,0,8), nocell(4,0,8), nocell(5,0,8), nocell(6,0,8), nocell(7,0,8), cell(8,0,8), nocell(0,1,8), nocell(1,1,8), cell(2,1,8), nocell(3,1,8), nocell(4,1,8), nocell(5,1,8), nocell(6,1,8), nocell(7,1,8), nocell(8,1,8), nocell(0,2,8), nocell(1,2,8), nocell(2,2,8), nocell(3,2,8), nocell(4,2,8), cell(5,2,8), nocell(6,2,8), nocell(7,2,8), nocell(8,2,8), cell(0,3,8), nocell(1,3,8), nocell(2,3,8), nocell(3,3,8), nocell(4,3,8), nocell(5,3,8), nocell(6,3,8), nocell(7,3,8), nocell(8,3,8), nocell(0,4,8), nocell(1,4,8), nocell(2,4,8), nocell(3,4,8), nocell(5,4,8), nocell(6,4,8), nocell(7,4,8), nocell(8,4,8), nocell(0,5,8), nocell(1,5,8), nocell(2,5,8), nocell(3,5,8), nocell(4,5,8), nocell(5,5,8), cell(6,5,8), nocell(7,5,8), nocell(8,5,8), nocell(0,6,8), nocell(1,6,8), nocell(2,6,8), nocell(3,6,8), nocell(4,6,8), nocell(5,6,8), nocell(6,6,8), cell(7,6,8), nocell(8,6,8), nocell(0,7,8), nocell(1,7,8), nocell(2,7,8), cell(3,7,8), nocell(4,7,8), nocell(5,7,8), nocell(6,7,8), nocell(7,7,8), nocell(8,7,8), nocell(0,8,8), nocell(2,8,8), nocell(3,8,8), nocell(4,8,8), nocell(5,8,8), nocell(6,8,8), nocell(7,8,8), nocell(8,8,8), nocell(0,0,9), nocell(1,0,9), nocell(2,0,9), nocell(3,0,9), cell(4,0,9), nocell(5,0,9), nocell(6,0,9), nocell(7,0,9), nocell(8,0,9), nocell(0,1,9), nocell(1,1,9), nocell(2,1,9), nocell(3,1,9), nocell(4,1,9), nocell(5,1,9), nocell(6,1,9), nocell(7,1,9), cell(8,1,9), nocell(0,2,9), nocell(1,2,9), nocell(3,2,9), nocell(4,2,9), nocell(5,2,9), nocell(6,2,9), nocell(7,2,9), nocell(8,2,9), nocell(0,3,9), nocell(1,3,9), nocell(2,3,9), nocell(3,3,9), nocell(4,3,9), nocell(5,3,9), nocell(6,3,9), cell(7,3,9), nocell(8,3,9), nocell(0,4,9), nocell(1,4,9), nocell(2,4,9), nocell(3,4,9), nocell(4,4,9), cell(5,4,9), nocell(6,4,9), nocell(7,4,9), nocell(8,4,9), nocell(0,5,9), cell(1,5,9), nocell(2,5,9), nocell(3,5,9), nocell(4,5,9), nocell(5,5,9), nocell(6,5,9), nocell(7,5,9), nocell(8,5,9), nocell(0,6,9), nocell(1,6,9), nocell(2,6,9), nocell(4,6,9), nocell(5,6,9), nocell(6,6,9), nocell(7,6,9), nocell(8,6,9), nocell(1,7,9), nocell(2,7,9), nocell(3,7,9), nocell(4,7,9), nocell(5,7,9), nocell(6,7,9), nocell(7,7,9), nocell(8,7,9), nocell(0,8,9), nocell(1,8,9), nocell(2,8,9), nocell(3,8,9), nocell(4,8,9), nocell(5,8,9), cell(6,8,9), nocell(7,8,9), nocell(8,8,9), assigned(0,1), assigned(0,2), assigned(0,3), assigned(0,4), assigned(0,6), assigned(0,8), assigned(1,0), assigned(1,2), assigned(1,3), assigned(1,5), assigned(1,6), assigned(1,7), assigned(2,0), assigned(2,1), assigned(2,4), assigned(2,5), assigned(2,7), assigned(2,8), assigned(3,0), assigned(3,1), assigned(3,4), assigned(3,5), assigned(3,7), assigned(3,8), assigned(4,0), assigned(4,2), assigned(4,3), assigned(4,5), assigned(4,6), assigned(4,7), assigned(5,1), assigned(5,2), assigned(5,3), assigned(5,4), assigned(5,6), assigned(5,7), assigned(5,8), assigned(6,1), assigned(6,2), assigned(6,3), assigned(6,4), assigned(6,5), assigned(6,6), assigned(6,8), assigned(7,0), assigned(7,3), assigned(7,4), assigned(7,5), assigned(7,6), assigned(7,7), assigned(8,0), assigned(8,1), assigned(8,3), assigned(8,4), assigned(8,5), assigned(8,7), assigned(8,8)}\n", "")
    