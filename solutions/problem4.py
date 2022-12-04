from typing import NamedTuple


class Section(NamedTuple):
    start: int
    end: int


def main():
    ans = 0
    ans1 = 0
    with open("inputs/day4input.txt") as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            sections = parse_input(line)
            if is_section_contained(sections[0], sections[1]):
                ans += 1
            if do_sections_overlap(sections[0], sections[1]):
                ans1 += 1
    print(ans)
    print(ans1)


def parse_input(line: str) -> list[Section, Section]:
    line = line.strip("\n")
    sections = line.split(",")
    ret = []
    for section in sections:
        parts = section.split("-")
        ret.append(Section(int(parts[0]), int(parts[1])))
    return ret


def is_section_contained(a: Section, b: Section) -> bool:
    if a.start <= b.start and a.end >= b.end:
        return True
    if b.start <= a.start and b.end >= a.end:
        return True
    return False


def do_sections_overlap(a: Section, b: Section) -> bool:
    return not max(a.start, b.start) > min(a.end, b.end)


if __name__ == "__main__":
    main()
