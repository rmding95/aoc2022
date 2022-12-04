from collections import defaultdict


def main():
    part_2()


def part_1() -> None:
    priorities = 0
    with open("inputs/day3input.txt") as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            line = line.strip("\n")
            first = line[0 : len(line) // 2]
            second = line[len(line) // 2 :]
            chars = defaultdict(int)
            for c in first:
                if chars[c] == 0:
                    chars[c] += 1
            for c in second:
                if chars[c] == 1:
                    priorities += char_to_priority_score(c)
                    chars[c] += 1
    print(priorities)


def part_2() -> None:
    priorities = 0
    with open("inputs/day3input.txt") as f:
        lines = f.readlines()
        for i in range(len(lines) // 3):
            first = lines[i * 3].strip("\n")
            second = lines[i * 3 + 1].strip("\n")
            third = lines[i * 3 + 2].strip("\n")
            chars = defaultdict(int)
            for c in first:
                if chars[c] == 0:
                    chars[c] += 1
            for c in second:
                if chars[c] == 1:
                    chars[c] += 1
            for c in third:
                if chars[c] == 2:
                    priorities += char_to_priority_score(c)
                    break
    print(priorities)


def char_to_priority_score(c: str) -> int:
    # a:z - 1:26
    # A:Z - 27:52
    if c.islower():
        return ord(c) - ord("a") + 1
    return ord(c) - ord("A") + 27


if __name__ == "__main__":
    main()
