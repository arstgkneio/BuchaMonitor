import random

window = []
max = 0
maxcount = 0
maxwin = 25

statCache = 0
statNonCache = 0

def addNum(n):
    global window
    global max
    global maxcount
    if len(window) == maxwin:
        m = window[0]
        window = window[1:]
        if maxcount > 0 and m == max:
            maxcount = maxcount - 1

    window.append(n)

    if len(window) == 1:
        max = n
        maxcount = 1
        return

    if maxcount > 0 and n > max:
        max = n
        maxcount = 1
        return

    if maxcount > 0 and n == max:
        maxcount = maxcount + 1

def getMax():
    global max
    global maxcount
    global statCache
    global statNonCache

    if len(window) == 0:
        return None

    if maxcount > 0:
        statCache = statCache + 1
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
    statNonCache = statNonCache + 1

    return max

# random.seed()
# for i in range(1000000):
#     val = int(1000 * random.random())
#     addNum(val)
#     newmax = getMax()

# print("%d cached, %d non-cached"%(statCache,statNonCache))