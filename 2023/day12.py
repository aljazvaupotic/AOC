from functools import cache


@cache
def solve(s, in_loop, remain):
    if not s:
        if in_loop is None and len(remain) == 0:
            return 1
        if len(remain) == 1 and in_loop is not None and in_loop == remain[0]:
            return 1
        return 0
    possible_more = 0
    for ch in s:
        if ch == '#' or ch == '?':
            possible_more += 1
    if in_loop is not None and possible_more + in_loop < sum(remain):
        return 0
    if in_loop is None and possible_more < sum(remain):
        return 0
    if in_loop is not None and len(remain) == 0:
        return 0
    poss = 0
    if s[0] == '.' and in_loop is not None and in_loop != remain[0]:
        return 0
    if s[0] == '.' and in_loop is not None:
        poss += solve(s[1:], None, remain[1:])
    if s[0] == '?' and in_loop is not None and in_loop == remain[0]:
        poss += solve(s[1:], None, remain[1:])
    if (s[0] == '#' or s[0] == '?') and in_loop is not None:
        poss += solve(s[1:], in_loop + 1, remain)
    if (s[0] == '?' or s[0] == '#') and in_loop is None:
        poss += solve(s[1:], 1, remain)
    if (s[0] == '?' or s[0] == '.') and in_loop is None:
        poss += solve(s[1:], None, remain)
    return poss


data = [x for x in open("input12.txt").read().strip().split('\n')]

p1 = 0
p2 = 0
for data_part in data:
    s = data_part.split(" ")[0]
    v = tuple([int(x) for x in data_part.split(" ")[1].split(",")])
    p1 += solve(s, None, v)
    news = ""
    for j in range(5):
        news += "?"
        news += s
    p2 += solve(news[1:], None, v * 5)
print(p1, p2)
