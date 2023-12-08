import math
from math import gcd
from functools import reduce


def pt1(ins, s, d):
    tmp = "AAA"
    while tmp != "ZZZ":
        i = ins[s % len(ins)]
        if i == "L":
            tmp = d[tmp][0]
        else:
            tmp = d[tmp][1]
        s += 1

    print(tmp, s)


def pt2(ins, starts, ends, d):
    ans = {i: 0 for i in ends}
    s = 0
    tmp = starts.copy()

    while any(value == 0 for value in ans.values()):
        i = ins[s % len(ins)]
        if i == "L":
            tmp = [d[item][0] for item in tmp]
        else:
            tmp = [d[item][1] for item in tmp]
        s += 1
        inter = set(tmp).intersection(set(ends))
        if inter:
            for i in inter:
                ans[i] = s
    print(math.lcm(*list(ans.values())))


# f = open("demo8.txt")
f = open("input8.txt")
data = f.readlines()

instructions = list(data[0].strip())
data.pop(0)
data.pop(0)
steps = 0
d = {}
last_letter = []
starts = []
ends = []
for pair in data:
    s, t = pair.strip().split("=")
    s = s.strip()
    if s[2] == "A":
        starts.append(s)
    if s[2] == "Z":
        ends.append(s)
    t = t.replace("(", "").replace(")", "").replace(" ", "")
    t = t.strip()
    t = tuple(t.split(","))
    d[s] = t

pt1(instructions,steps,d)
pt2(instructions, starts, ends, d)

