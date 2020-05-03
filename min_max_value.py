import random

window = []
max = 0
min = 0
maxcount = 0
mincount = 0
maxwin = 25

minStatCache = 0
maxStatCache = 0
minStatNonCache = 0
maxStatNonCache = 0

def addNum(n):
    global window
    global min
    global max
    global mincount
    global maxcount

    if len(window) == maxwin:
        m = window[0]
        window = window[1:]
        if maxcount > 0 and m == max:
            maxcount = maxcount - 1
        if mincount > 0 and m == min:
            mincount = mincount - 1

    window.append(n)

    if len(window) == 1:
        max = n
        min = n
        maxcount = 1
        mincount = 1
        return

    if maxcount > 0 and n > max:
        max = n
        maxcount = 1
        return

    if mincount > 0 and n < min:
        min = n
        mincount = 1
        return

    if maxcount > 0 and n == max:
        maxcount = maxcount + 1

    if mincount > 0 and n == min:
        mincount = mincount + 1

def getMax():
    global max
    global maxcount
    global maxStatCache
    global maxStatNonCache

    if len(window) == 0:
        return None

    if maxcount > 0:
        maxStatCache = maxStatCache + 1
        return max

    max = window[0]
    maxcount = 0
    for val in window:
        if val > max:
            max = val
            maxcount = 1
        else:
            if val == max:
                maxcount = maxcount + 1
    maxStatNonCache = maxStatNonCache + 1

    return max

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
    newmax = getMax()
    newmin = getMin()

print("the min is:", newmin)
print("the max is:", newmax)

#print("%d cached, %d non-cached"%(statCache,statNonCache))
