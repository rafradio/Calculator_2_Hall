import sys
import datetime

class Logger():
    stdout = sys.stdout

    def __init__(self):
        self.stdin = sys.stdin
        sys.stdout = self
        self.f = open('file.txt', 'a')

    def stop(self):
        sys.stdout = self.stdout
        sys.stdin.close()
        self.f.close()
        
    def readline(self, text):
        x = datetime.datetime.now()
        logstring = "Log - Day {}.{}.{}".format(x.strftime("%d"), x.strftime("%m"), x.strftime("%y"))
        logstring += " Time {}.{}.{}\n".format(x.strftime("%H"), x.strftime("%M"), x.strftime("%S"))

        line = self.stdin.readline()
        if line.rstrip() == "Exit": return line

        text += line + "\n"
        self.f.write(logstring + text)
        return line

    def write(self, text):
        self.stdout.write(text)

    def flush(self):
        pass


