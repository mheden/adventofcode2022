from utils import slurp, unpack, assertEq


gamepoints = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

handpoints = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def part1(data):
    return sum(
        gamepoints[(a, b)] + handpoints[b]
        for a, b in unpack(data, fn=lambda x: x.split(" "))
    )


def part2(data):
    whattoplay = {
        ("A", "Y"): "X",
        ("A", "Z"): "Y",
        ("A", "X"): "Z",
        ("B", "X"): "X",
        ("B", "Y"): "Y",
        ("B", "Z"): "Z",
        ("C", "Z"): "X",
        ("C", "X"): "Y",
        ("C", "Y"): "Z",
    }

    return sum(
        gamepoints[(a, whattoplay[(a, b)])] + handpoints[whattoplay[(a, b)]]
        for a, b in unpack(data, fn=lambda x: x.split(" "))
    )


filedata = slurp("02.txt")
testdata = """
A Y
B X
C Z
"""

print("#--- Day 2: Rock Paper Scissors: part1:", end=" ")

assertEq(part1(testdata), 15)
print(part1(filedata))

print("#--- Day 2: Rock Paper Scissors: part2:", end=" ")

assertEq(part2(testdata), 12)
print(part2(filedata))
