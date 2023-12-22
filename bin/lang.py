import json
import os
from coraos.log.file import LogFile


class Lang:
    def __init__(self):
        self.source = None
        self.source_file = None
        self.logFile = LogFile("org.cora.casil.lang", "./CASIL_LANG")
        self.logFile.process("org.cora.casil.lang.Lang.__init__()")

    def set_source(self, source_file: str | os.PathLike):
        self.source_file = source_file
        self.logFile.process("Got source file path.")

    def parse(self):
        with open(self.source_file, "r") as s:
            self.source = json.load(s)

    

