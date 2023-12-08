from collections import Counter


def get_str(cards):
    values = set(cards)
    s = []
    for card in values:
        s.append(cards.count(card))
    s = tuple(sorted(s, reverse=True))
    return STRENGTH.index(s)


def map_faces(x):
    return [value for char, value in FACES if x == char][0] if not x.isdigit() else int(x)


def swap_joker_to_max(cards, value):
    return [value if c == 0 else c for c in cards]


def change_joker_to_max(cards, counter):
    key = counter.most_common(1)[0][0]
    if key == 0:
        del counter[key]
        if counter:
            key = counter.most_common(1)[0][0]
    if key != 0:
        return get_str(swap_joker_to_max(cards, key))
    return get_str(cards)


def get_str_with_jokers(h):
    h = swap_j(h)
    c = Counter(h)
    return change_joker_to_max(h, c)


def swap_j(cards):
    for i, c in enumerate(cards):
        cards[i] = 0 if c == 11 else c
    return cards


def sum_tuple(t):
    total = 0
    for i, r in enumerate(t):
        total += (i + 1) * int(r[1])
    return total


def parse_cards(d):
    plays_pt1 = []
    plays_pt2 = []
    for e in d:
        hand = [map_faces(v) for v in e.strip().split(" ")[0]]
        hand_joker = hand.copy()
        bid = e.strip().split(" ")[1]
        strength = get_str(hand)
        plays_pt1.append((hand, bid, strength))
        jokers = get_str_with_jokers(hand_joker)
        plays_pt2.append((hand_joker, bid, jokers))
    return plays_pt1, plays_pt2


#
#
STRENGTH = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1), (3, 1, 1), (3, 2), (4, 1), (5,)]

FACES = [("A", 14), ("T", 10), ("J", 11), ("Q", 12), ("K", 13)]

# f = open("demo7.txt")
f = open("input7.txt")
data = f.readlines()
plays, joker = parse_cards(data)
plays.sort(key=lambda x: (x[2], tuple(x[0])))
joker.sort(key=lambda x: (x[2], tuple(x[0])))
print(sum_tuple(plays))
print(sum_tuple(joker))
