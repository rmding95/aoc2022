CYCLES = {"noop": 1, "addx": 2}
PICTURE_LEN = 40
PICTURE_WIDTH = 6


def main():
    with open("inputs/day10input.txt") as f:
        instructions = f.read().splitlines()
        values = handle_instructions(instructions)
        ans = 0
        for i in range(20, 240, 40):
            ans += i * values[i - 1]
        print(ans)
        print(draw_picture(values))


def handle_instructions(instructions: list[str]) -> list[int]:
    register_value = 1
    values: list[int] = []
    for instruction in instructions:
        split = instruction.split(" ")
        if len(split) == 1:
            values.append(register_value)
        else:
            for _ in range(CYCLES["addx"]):
                values.append(register_value)
            register_value += int(split[1])
    return values


def draw_picture(values: list[int]) -> str:
    picture = ""
    for width in range(PICTURE_WIDTH):
        for length in range(PICTURE_LEN):
            cycle = PICTURE_LEN * width + length
            register_val = values[cycle]
            if length in range(register_val - 1, register_val + 2):
                picture += "#"
            else:
                picture += "."
            if length == PICTURE_LEN - 1:
                picture += "\n"
    return picture


if __name__ == "__main__":
    main()
