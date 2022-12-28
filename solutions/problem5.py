from collections import deque


def main():
    with open("inputs/day5input.txt") as f:
        data = f.read()
        crates = parse_crates(data)
        queue = [deque(x) for x in crates]
        # part 1
        run_instructions(data, crates)
        print("".join(x[-1] for x in crates))
        # part 2
        run_instructions_queue(data, queue)
        print("".join(x[-1] for x in queue))


def parse_crates(data: str) -> list[list[str]]:
    lines = data.split("\n")
    crates = []
    for line in lines:
        line = line.strip("\n")
        if len(line) == 0:
            continue
        idx = 0
        crate_step = True
        stack = []
        if line[1] == "1":
            break
        while idx < len(line):
            if crate_step:
                if line[idx] == "[":
                    stack.append(line[idx + 1])
                else:
                    stack.append("")
                crate_step = False
                idx += 3
            else:
                idx += 1
                crate_step = True
        crates.append(stack)
    stacks = [[] for _ in range(len(crates[0]))]
    for i in range(len(crates) - 1, -1, -1):
        for idx, val in enumerate(crates[i]):
            if val == "":
                continue
            stacks[idx].append(val)
    return stacks


def parse_instructions(data: str) -> list[tuple[int, int, int]]:
    lines = data.split("\n\n")[1]
    instructions = lines.split("\n")
    parsed = []
    for instruction in instructions:
        if len(instruction) == 0:
            continue
        split = instruction.split(" ")
        parsed.append((int(split[1]), int(split[3]) - 1, int(split[5]) - 1))
    return parsed


def run_instructions(data: str, crates: list[list[str]]) -> None:
    instructions = parse_instructions(data)
    for instruction in instructions:
        quantity, start_idx, end_idx = instruction
        for _ in range(quantity):
            val = crates[start_idx].pop()
            crates[end_idx].append(val)


def run_instructions_queue(data: str, queue: list[deque[str]]) -> None:
    instructions = parse_instructions(data)
    for instruction in instructions:
        quantity, start_idx, end_idx = instruction
        if quantity > 1:
            temp = deque()
            for _ in range(quantity):
                temp.appendleft(queue[start_idx].pop())
            queue[end_idx].extend(temp)
        else:
            val = queue[start_idx].pop()
            queue[end_idx].append(val)


if __name__ == "__main__":
    main()
