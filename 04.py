from utils import slurp, unpack, assertEq, numbers


def part1(data):
    def overlap(s1, e1, s2, e2):
        if s1 <= s2 and e1 >= e2:
            return True
        elif s2 <= s1 and e2 >= e1:
            return True
        else:
            return False

    return sum(overlap(*numbers(row)) for row in unpack(data))


def part2(data):
    def overlap(s1, e1, s2, e2):
        if s1 <= s2 <= e1:
            return True
        elif s1 <= e2 <= e1:
            return True
        elif s2 <= s1 <= e2:
            return True
        elif s2 <= e1 <= e2:
            return True
        else:
            return False

    return sum(overlap(*numbers(row)) for row in unpack(data))


filedata = slurp("04.txt")
testdata = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

print("Day 4: Camp Cleanup: part1:", end=" ")

assertEq(part1(testdata), 2)
print(part1(filedata))

print("Day 4: Camp Cleanup: part2:", end=" ")

assertEq(part2(testdata), 4)
print(part2(filedata))
