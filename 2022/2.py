score = {
    'A X': 4,  # kamen izenačeno     3+1
    'B X': 1,  # kamen poraz         0+1
    'C X': 7,  # kamen zmaga         6+1
    'A Y': 8,  # papir zmaga         6+2
    'B Y': 5,  # papir izenačeno     3+2
    'C Y': 2,  # papir poraz         0+2
    'A Z': 3,  # škarje poraz        0+3
    'B Z': 9,  # škarje zmaga        6+3
    'C Z': 6,  # škarje izenačeno    3+3
}

score_second_part = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}
points = {
    'A': 1,
    'B': 2,
    'C': 3,
}
permutateLost = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

permutateWin = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

totalScore = 0
totalScore2 = 0
for line in open("input_2.txt"):
    play = line.strip()
    totalScore += score[play]
    play = play.split()
    if play[1] == 'X':
        totalScore2 += points[permutateLost[play[0]]]
    elif play[1] == 'Y':
        totalScore2 += points[play[0]] + 3
    else:
        totalScore2 += points[permutateWin[play[0]]] + 6

print(totalScore, totalScore2)
