import inputModule

def controller(objLog):
    strLine = True
    while strLine:
        lineCheck = inputModule.inputMethod(objLog)
        if 'Exit' == lineCheck.rstrip():
            break