import random

window = []
min = 0
mincount = 0
maxwin = 25

minStatCache = 0
minStatNonCache = 0

def addNum(n):
    global window
    global min
    global mincount
    if len(window) == maxwin:
        m = window[0]
        window = window[1:]
        if mincount > 0 and m == min:
            mincount = mincount - 1

    window.append(n)

    if len(window) == 1:
        min = n
        mincount = 1
        return

    if mincount > 0 and n < min:
        min = n
        mincount = 1
        return

    if mincount > 0 and n == min:
        mincount = mincount + 1

def getMin():
    global min
    global mincount
    global minStatCache
    global minStatNonCache

    if len(window) == 0:
        return None

    if mincount > 0:
        minStatCache = minStatCache + 1
        return min

    min = window[0]
    mincount = 0
    for val in window:
        if val < min:
            min = val
            mincount = 1
        else:
            if val == min:
                mincount = mincount + 1
    minStatNonCache = minStatNonCache + 1

    return min

random.seed()
for i in range(1000000):
    val = int(1000 * random.random())
    addNum(val)
    newmin = getMin()
print(newmin)
print("%d cached, %d non-cached"%(minStatCache,minStatNonCache))
