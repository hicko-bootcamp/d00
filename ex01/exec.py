import sys


argument = sys.argv
argument.pop(0)
result = ' '.join(argument).swapcase()[::-1]
if len(argument):
    print(result)
