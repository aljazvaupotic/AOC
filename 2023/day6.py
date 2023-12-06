import numpy
import time
import math

TEST = ["Time:      7  15   30",
        "Distance:  9  40  200"]


def count_optimized(t, d):
    c = 0
    for x in range(0, t // 2):
        time_remaining = t - x
        speed = x
        if speed * time_remaining > d:
            c += 2
    if t % 2 == 0:
        c += 1
    return c


###
# button
# f(x) = ((time - button)*button - distance
# f(x) = button2 + time*button - distance
# no of integers between where f(x) = 0 is number of times
# x1 =  (time + sqrt(time2 - 4 * distance)) / 2
# x2 =  (time - sqrt(time2 - 4 * distance)) / 2
##
def quadratic(t, d):
    sqrt = math.sqrt(int(t) ** 2 - 4 * int(d))
    return math.ceil((t + sqrt) / 2) - math.floor((t - sqrt) / 2) - 1


def count_ways(t, d):
    ways = []
    for i, y in enumerate(t):
        c = 0
        for x in range(0, y):
            time_remaining = y - x
            speed = x
            if speed * time_remaining > d[i]:
                c += 1
        ways.append(c)
    return numpy.prod(ways)


start_time = time.time()
f = open("input6.txt")
data = f.readlines()
# data = TEST
pt1_time = time.time()

times = []
distances = []
holdingSeconds = []
for entry in data:
    tmp = entry.split(":")
    name = tmp[0]
    values = list(filter(None, tmp[1].strip().split(" ")))
    if name == 'Time':
        times = [int(i) for i in values]
    else:
        distances = [int(i) for i in values]

print("PT 1:", count_ways(times, distances))
print("--- %s seconds ---" % (time.time() - pt1_time))
pt2_time = time.time()

timeLeft = ""
dist = ""
for entry in data:
    tmp = entry.split(":")
    name = tmp[0]
    values = list(filter(None, tmp[1].strip().split(" ")))

    if name == 'Time':
        timeLeft = int(timeLeft.join(values))
    else:
        dist = int(dist.join(values))
print("PT 2:", count_optimized(timeLeft, dist))
print("--- %s seconds ---" % (time.time() - pt2_time))
print(" Total run time")
print("--- %s seconds ---" % (time.time() - start_time))
q_time = time.time()
print("Quadratic :", quadratic(timeLeft, dist))
print("--- %s seconds ---" % (time.time() - q_time))
