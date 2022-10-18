import logModule
import inputModule
import sys

if __name__ == '__main__':

    log = logModule.Logger()
    strLine = True
    while strLine:
        xx = inputModule.inputMethod(log)
        if 'Exit' == xx.rstrip():
            break

        
    # print(xx)

    log.stop()