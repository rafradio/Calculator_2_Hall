from math import factorial
import re


def Calculate(inStr):
    calcStr = inStr
    calcStr = calcStr.replace("^","**")
    if re.findall("\d*\!",inStr):
        for f in re.findall("\d*\!",inStr):
            calcStr = inStr.replace(f,f"factorial({f.replace('!','')})")
    return eval(calcStr)
