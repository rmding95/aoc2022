from collections import defaultdict

# change to 4 for part 1 answer
BUFFER_LEN = 14


def main():
    with open("inputs/day6input.txt") as f:
        data = f.read()
        print(find_buffer(data))


def find_buffer(text: str) -> int:
    i = 0
    while i < len(text) - BUFFER_LEN:
        window = set(text[i : i + BUFFER_LEN])
        if len(window) != BUFFER_LEN:
            i += 1
            continue
        return i + BUFFER_LEN
    return -1


if __name__ == "__main__":
    main()
