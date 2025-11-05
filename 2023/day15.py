import time


def solve(d):
    vals = []
    boxes = {}
    focusing_power = 0
    for instruction in d:
        vals.append(get_hash_value(instruction))

        if '=' in instruction:
            lens_to_insert = instruction.split('=')
            box_number = get_hash_value(lens_to_insert[0])
            if box_number in boxes:
                existing_lens = [boxes[box_number].index(lens) for lens in boxes[box_number] if
                                 lens_to_insert[0] in lens]
                if len(existing_lens) == 0:
                    boxes[box_number] += [lens_to_insert]
                else:
                    boxes[box_number][existing_lens[0]] = lens_to_insert
            else:
                boxes[box_number] = [lens_to_insert]


        elif '-' in instruction:
            label = instruction[:-1]
            box_number = get_hash_value(label)
            if box_number in boxes:
                boxes[box_number] = [lens for lens in boxes[box_number] if label not in lens]

    for key, value in boxes.items():
        if len(value) != 0:
            for i, lens in enumerate(value):
                focusing_power += (key + 1) * (i + 1) * int(lens[1])

    return sum(vals), focusing_power


def get_hash_value(string):
    return sum([(ord(char)) * (17 ** (len(string) - i)) % 256 for i, char in enumerate(string)]) % 256


st = time.time()
f = open('input15.txt')
# f = open('demo15.txt')
data = f.read().strip().split(',')
pt1, pt2 = solve(data)
print('Pt 1:', pt1)
print('Pt 2:', pt2)

print("--- %s seconds ---" % (time.time() - st))
