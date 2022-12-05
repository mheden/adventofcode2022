from utils import slurp, unpack, assertEq, numbers


def parse_init(init):
    init = init.split("\n")
    num_stacks = numbers(init[-1])[-1]
    stacks = []
    for _ in range(num_stacks):
        stacks.append([])
    for row in reversed(init[:-1]):
        for stack in range(num_stacks):
            c = row[1 + stack * 4]
            if c != " ":
                stacks[stack].append(c)
    return stacks


def part1(data):
    init, moves = data.split("\n\n")
    stacks = parse_init(init)

    for move in unpack(moves):
        num, from_, to_ = numbers(move)
        for _ in range(num):
            stacks[to_ - 1].append(stacks[from_ - 1].pop())

    return "".join(s.pop() for s in stacks)


def part2(data):
    init, moves = data.split("\n\n")
    stacks = parse_init(init)

    for move in unpack(moves):
        num, from_, to_ = numbers(move)
        nums = []
        for _ in range(num):
            nums.append(stacks[from_ - 1].pop())
        stacks[to_ - 1] += list(reversed(nums))

    return "".join(s.pop() for s in stacks)


filedata = slurp("05.txt")
testdata = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

print("Day 5: Supply Stacks: part1:", end=" ")

assertEq(part1(testdata), "CMZ")
print(part1(filedata))

print("Day 5: Supply Stacks: part2:", end=" ")

assertEq(part2(testdata), "MCD")
print(part2(filedata))
