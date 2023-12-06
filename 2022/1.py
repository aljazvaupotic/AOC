s = 0
maxS = 0
elfNumber = 0
elf = []
for line in open("input_1.txt"):
    if line.strip():
        v = int(line)
        s += v
    else:
        maxS = max(maxS,s)
        elf.append(s)
        s = 0
        elfNumber += 1

print (maxS)
elf.sort()
print(sum(elf[-3:]))