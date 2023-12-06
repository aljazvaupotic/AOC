tmp = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
       "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
       "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
       "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
       "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
       "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

f = open("input4.txt")
data = f.readlines()
#data = tmp
total = []
for line in data:
    x = line.strip().split(":")
    gameNo = x[0].split()[1]
    numbers = x[1].strip().split("|")
    winning = list(map(int, numbers[0].split()))
    chosen = list(map(int, numbers[1].split()))
    score = 0
    for num in winning:
        if num in chosen:
            score = 1 if score == 0 else score * 2

    total.append(score)

print(sum(total))

numberOfTickets = [1]*len(data)

for i,line in enumerate(data):
    x = line.strip().split(":")
    gameNo = int(x[0].split()[1])
    numbers = x[1].strip().split("|")
    winning = list(map(int, numbers[0].split()))
    chosen = list(map(int, numbers[1].split()))
    multiplyThisMany = 0
    for num in winning:
        if num in chosen:
            multiplyThisMany += 1
    for x in range(i+1, i+multiplyThisMany+1):
        if x < len(numberOfTickets):
            numberOfTickets[x] += numberOfTickets[i]
print(sum(numberOfTickets))