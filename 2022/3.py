def find_repeating(triple):
    repeating_characters = set(triple[0])
    repeating_characters = repeating_characters.intersection(triple[1])
    repeating_characters = repeating_characters.intersection(triple[2])

    return list(repeating_characters)




data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

# prekat1 = [x[0:len(x) // 2].strip() for x in open("input_3.txt")]
# prekat2 = [x[len(x) // 2:].strip() for x in open("input_3.txt")]

data = [x.strip() for x in open("input_3.txt")]

# zip(
# *[(line[:len(line) // 2].strip(), line[len(line) // 2:].strip()) for line in open("input_3.txt")])

# Initialize a dictionary to store item type priorities
item_priorities = {}

# Lowercase item types a through z have priorities 1 through 26
for i, item_type in enumerate(range(ord('a'), ord('z') + 1), start=1):
    item_priorities[chr(item_type)] = i

# Uppercase item types A through Z have priorities 27 through 52
for i, item_type in enumerate(range(ord('A'), ord('Z') + 1), start=27):
    item_priorities[chr(item_type)] = i

t = 0
for i in range(0,len(data), 3):
    matching = find_repeating([data[i],data[i+1],data[i+2]])
    t += item_priorities[matching[0]]

print(t)