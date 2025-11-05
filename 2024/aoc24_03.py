import re
with open("demo3.txt") as file:
    data = file.read()
    pattern = r"mul\((\d+),\s*(\d+)\)"
    match = re.findall(pattern, data)
    k = 0
    t = 0
    for m in match:
        k += int(m[0]) * int(m[1])

    do_muls = data.split("do()")
    for do_mul in do_muls:
        do = do_mul.split("don't()")[0]
        t += sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", do))

    print(k, t)