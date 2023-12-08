def get_single_seeds(lines):
    return [int(seed) for seed in lines[0].split(': ')[1].split()]


def get_seed_ranges(lines):
    all_ranges = lines[0].split(': ')[1].split()
    seed_ranges = []
    for i in range(0, len(all_ranges)-1, 2):
        seed_from, seed_to = int(all_ranges[i]), int(all_ranges[i+1])
        seed_ranges.append((seed_from, seed_to))
    return seed_ranges


def get_map(lines, map_id):
    data = lines[map_id]
    map_of_ranges = {}
    for map_id, dataset in enumerate(data.split('\n')[1:]):
        map_of_ranges[map_id] = [int(number) for number in dataset.split()]
    return map_of_ranges


def get_maps(full_data):
    return [get_map(full_data, map_id) for map_id in range(1,8)]


def get_seed_range_id(seed, map_of_ranges):
    for range_id, data in map_of_ranges.items():

        _, source, length = data
        if source <= seed < source + length:
            return range_id
    return -1


def map_numbers(current, map_of_ranges):
    range_id = get_seed_range_id(current, map_of_ranges)
    if range_id == -1:
        return current

    destination, source, _ = map_of_ranges[range_id]
    delta = destination - source

    return current + delta


def find_smallest(full_data):
    seeds = get_single_seeds(full_data)
    all_maps = get_maps(full_data)
    minimum = -1

    for current in seeds:
        for sth_to_sth in all_maps:
            current = map_numbers(current, sth_to_sth)
        if minimum == -1 or current < minimum:
            minimum = current

    return minimum


def smallest_in_range(rng, all_maps, step):
    minimum = (-1, -1)
    for current in range(rng[0], rng[0]+rng[1], step):
        tested_seed = current
        for sth_to_sth in all_maps:
            current = map_numbers(current, sth_to_sth)
        if minimum[0] == -1 or current < minimum[0]:
            minimum = (current, tested_seed)
    return minimum


def find_smallest_in_ranges(full_data):
    seed_ranges = get_seed_ranges(full_data)
    all_maps = get_maps(full_data)
    minimum = -1

    step = 100_000_000
    stop_step = 10_000

    while step >= stop_step:
        for seed_range in seed_ranges:
            range_minimum = smallest_in_range(seed_range, all_maps, step)
            if minimum == -1 or range_minimum < minimum:
                minimum = range_minimum
        candidate_range = (minimum[1] - step, step * 10)
        seed_ranges = [candidate_range]
        step //= 10

    final_candidate = (seed_ranges[0][0] - step, step * 10)

    return smallest_in_range(final_candidate, all_maps, 1)[0]



f = open("input5.txt")
#f = open("demo5.txt")
data = f.read()
paragraphs = data.split('\n\n')

print(find_smallest(paragraphs))
print(find_smallest_in_ranges(paragraphs))
