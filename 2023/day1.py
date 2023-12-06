import re

numbers = []

for line in open("input1.txt"):
    x = re.findall("[0-9]+", line)
    number = "".join(x)
    # if len(number) != 1:
    number = number[0] + number[-1]
    numbers.append(int(number))

print(sum(numbers))

number_words = ["one", "two", "three", "four", "five","six", "seven", "eight", "nine"]


numbers = []
for line in open("input1.txt"):
    i = 1;
    t = line
    for num in number_words:
        repl = num + str(i) + num
        t = t.replace(num, repl)
        i += 1
    f = re.findall("[0-9]+", t)

    number = "".join(f)
    number = number[0] + number[-1]

    print(line,t, number)

    numbers.append(int(number))


print(sum(numbers))
