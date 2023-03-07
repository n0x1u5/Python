import sys
import re
import os

table = ""
comment = ""
duration = ""

class Parser:
    def __init__(self):
        self._table = ''
        self._comment = ''
        self._duration = ''

    def process_line(self, line):
        x = re.match("Command: UPDATE STATISTICS (.+)", line)
        if x:
            self._table = self.extract_Table(x.group(1))
            return
        x = re.match("^Comment: (.+)", line)
        if x:
            self._comment = x.group(0)
            return
        x = re.match("^Duration: (\d\d:\d\d:\d\d)", line)
        if x:
            self._duration = x.group(1)

    def clear(self):
        self._table = ''
        self._comment = ''
        self._duration = ''

    def get_data(self):
        if self._table!='' and self._comment!='' and self._duration!='':
            result = f"{self._table}\t{self._comment}\t{self._duration}"
            self.clear()
            return result

    def extract_Table(self, line):
        x = re.match('\[(\w+)\]\.\[(\w+)\]', line)
        if x:
            return f'{x.group(0)}'

if __name__ == "__main__":
    parser = Parser()
    if len(sys.argv)!=2:
        print("log file missing")
        exit(1)
    f = open(sys.argv[1],'r')
    while True:
        line = f.readline()
        if not line:
            break
        parser.process_line(line.strip())
        data = parser.get_data()
        if data:
            print(data)
    f.close()