# Supply stacks
import re

def parse_crates(c):
    for x in c:
        print(x)

def parse_moves(moves):
    tmp =  [re.findall(r"\d+",i) for i in moves.split('\n')]
    instructions = []
    for line in tmp:
        instructions.append(tuple(line))
    return instructions

def get_instructions(file):
    crates, moves = file.read().split("\n\n")
    stacks = parse_crates(crates)
    instructions = parse_moves(moves)


f = open("demo_5.txt")
#f = open("input_5.txt.txt")


get_instructions(f)



