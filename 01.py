from utils import slurp, unpack, assertEq


def part1(s):
    return max(sum(unpack(x, fn=int)) for x in unpack(s, sep="\n\n"))


def part2(s):
    calories = (sum(unpack(x, fn=int)) for x in unpack(s, sep="\n\n"))
    return sum(sorted(calories, reverse=True)[0:3])


filedata = slurp("01.txt")
testdata = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

print("#--- Day 1: Calorie Counting: part1:", end=" ")

assertEq(part1(testdata), 24000)
print(part1(filedata))

print("#--- Day 1: Calorie Counting: part2:", end=" ")

assertEq(part2(testdata), 45000)
print(part2(filedata))
