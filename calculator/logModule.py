import sys
import datetime

class Logger():
    stdout = sys.stdout

    def __init__(self):
        self.stdin = sys.stdin
        sys.stdout = self
        sys.stdin = self
        self.f = open('file.txt', 'a')
        self.f.write("\n")

    def stop(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
        #sys.stdin.close()
        self.f.close()
        
    def readline(self, text = "Please input string for calculation: "):
        logstring = self.LogDayTime()

        line = self.stdin.readline()
        if line.rstrip() == "Exit": return line

        text += line + "\n"
        self.f.write(logstring + text)
        return line

    def write(self, text):
        logstring = self.LogDayTime()

        if "Result" in text: self.f.write(logstring + text + "\n")
        else: self.stdout.write(text)

    def flush(self):
        pass

    def LogDayTime(self):
        x = datetime.datetime.now()
        logstring = "Log - Day {}.{}.{}".format(x.strftime("%d"), x.strftime("%m"), x.strftime("%y"))
        logstring += " Time {}.{}.{}\n".format(x.strftime("%H"), x.strftime("%M"), x.strftime("%S"))
        return logstring


