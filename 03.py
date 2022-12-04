from utils import slurp, unpack, assertEq, lmap, chunks, take


def prio(letter):
    if "a" <= letter <= "z":
        return ord(letter) - ord("a") + 1
    else:
        return ord(letter) - ord("A") + 27


def part1(data):
    sum_ = 0
    for row in unpack(data):
        compartments = lmap(set, chunks(row, len(row) // 2))
        sum_ += prio((compartments[0] & compartments[1]).pop())
    return sum_


def part2(data):
    data = unpack(data)
    sum_ = 0
    while len(data) > 0:
        rows = lmap(set, take(data, 3))
        sum_ += prio((rows[0] & rows[1] & rows[2]).pop())
    return sum_


filedata = slurp("03.txt")
testdata = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

print("#--- Day 3: Rucksack Reorganization: part1:", end=" ")

assertEq(part1(testdata), 157)
print(part1(filedata))

print("#--- Day 3: Rucksack Reorganization: part2:", end=" ")

assertEq(part2(testdata), 70)
print(part2(filedata))
