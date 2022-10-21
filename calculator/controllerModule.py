import inputModule
import calculate

def controller(objLog):
    strLine = True
    while strLine:
        lineCheck = inputModule.inputMethod(objLog)
        if 'Exit' == lineCheck.rstrip():
            break
        
        resultString = calculate.calcPrint(lineCheck)
        print(resultString)
    