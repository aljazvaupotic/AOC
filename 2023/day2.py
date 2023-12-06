rules = {"red": 12, "green": 13, "blue": 14}
games = []

txt = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
       "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
       "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
       "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
       "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
numOfCubes = 0
for line in open("input2.txt"):

    x = line.strip().split(":")
    gameNo = x[0]
    isValid = True
    game = x[1]
    minCubes = [0, 0, 0]
    pulled = game.split(";")
    for turn in pulled:
        color = turn.split(",")
        for c in color:
            c = c.strip().split()
            if c[1] == "red":
                minCubes[0] = max(int(c[0]), minCubes[0])
            elif c[1] == "blue":
                minCubes[1] = max(int(c[0]), minCubes[1])
            else:
                minCubes[2] = max(int(c[0]), minCubes[2])

            for x in rules.items():
                if c[1] == x[0]:
                    num = int(c[0])
                    if num > x[1]:
                        isValid = False
                        break
    print((minCubes[0] * minCubes[1] * minCubes[2]))
    numOfCubes += (minCubes[0] * minCubes[1] * minCubes[2])

    if isValid:
        games.append(int(gameNo.replace("Game ", "")))

print(sum(games), numOfCubes)
