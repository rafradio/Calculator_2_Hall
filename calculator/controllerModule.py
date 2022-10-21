import inputModule
import calcModule

def controller(objLog):
    strLine = True
    while strLine:
        lineCheck = inputModule.inputMethod(objLog)
        if 'Exit' == lineCheck.rstrip():
            break
        
        resultString = calcModule.Calculate(lineCheck)
        resultString = "Result is equal: " + str(resultString)
        print(resultString)
    