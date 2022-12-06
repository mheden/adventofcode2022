from utils import slurp, assertEq, unique


def startpos(buffer, n):
    for i in range(0, len(buffer) - n):
        if len(unique(buffer[i : i + n])) == n:
            return i + n
    return -1


filedata = slurp("06.txt")

print("Day 6: Tuning Trouble: part1:", end=" ")

assertEq(startpos("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4), 7)
assertEq(startpos("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
assertEq(startpos("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
assertEq(startpos("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
assertEq(startpos("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)

print(startpos(filedata, 4))

print("Day 6: Tuning Trouble: part2:", end=" ")

assertEq(startpos("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
assertEq(startpos("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
assertEq(startpos("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
assertEq(startpos("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
assertEq(startpos("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)

print(startpos(filedata, 14))
