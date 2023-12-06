data = [x.strip() for x in open("input_4.txt")]

m= 0

overlap = 0
for line in data:
    pairs = line.split(",")
    first = [int(p) for p in pairs[0].split("-")]
    second = [int(p) for p in pairs[1].split("-")]
    print(first,second)
    if(first[0]<= second[0] and first[1]>= second[1]) or (first[0]>= second[0] and first[1]<= second[1]) :
        m += 1

    if first[1] >= second[0] and second[1] >= first[0]:
        overlap += 1
print(m)
print(overlap)

