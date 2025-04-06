import time
import sys

#0.005
def smartPrint(string, speed=0.025):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print('')


def showArrayValues (array, comment=''):
    if comment != '':
        smartPrint(comment)
    for i in range(0, len(array), 1):
       smartPrint(str(i) + ") " + array[i]) 


def inputHandler(i):
    try:
        int(i)
        return int(i)
    except ValueError:
        n()
        smartPrint("Ошибка! Введён некорректный тип данных.")
        #smartPrint("Попробуйте ещё раз.")
        return -1



def n ():
    print('')

def die():
    sys.exit()