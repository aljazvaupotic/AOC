l = []
r = []

for line in open("demo1.txt"):
    left, right = map(int, line.split('   '))
    l.append(left)
    r.append(right)

l.sort()
r.sort()
td = 0
f  = 0
for i in range(len(l)):
    td += abs(l[i] - r[i])

    f += l[i] * r.count(l[i])
print(td, f)
