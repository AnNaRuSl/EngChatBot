import time
import sys

#0.005
def smartPrint(string, end = "#", speed = 0.015):
    string = string + end
    for char in string:
        if char == "#":
            n ()
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)


def showArrayValues (array, comment=''):
    if comment != '':
        smartPrint(comment)
    for i in range(0, len(array), 1):
       smartPrint(str(i + 1) + ") " + array[i]) 


def inputHandler(i):
    try:
        int(i)
        return int(i) - 1
    except ValueError:
        n()
        smartPrint("Ошибка! Введён некорректный тип данных.")
        #smartPrint("Попробуйте ещё раз.")
        return -1



def n ():
    print('')

def die():
    sys.exit()