from util import Point2D


DIRECTION_MAP: dict[str, tuple[int, int]] = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}
# change to 2 for part 1 answer
NUM_POINTS = 10


def main():
    visited: set[tuple[int, int]] = set([(0, 0)])
    points: list[Point2D] = []
    for _ in range(NUM_POINTS):
        points.append(Point2D(0, 0))
    with open("inputs/day9input.txt") as f:
        instructions = f.read().splitlines()
        for instruction in instructions:
            direction, steps = instruction.split(" ")
            update_positions(points, DIRECTION_MAP[direction], int(steps), visited)
    print(len(visited))


def update_positions(
    points: list[Point2D],
    direction: tuple[int, int],
    steps: int,
    visited: set[tuple[int, int]],
) -> None:
    head = points[0]
    for _ in range(steps):
        head.update_position(direction[0], direction[1])
        for idx, point in enumerate(points):
            if idx == 0:
                continue
            update_position(points[idx - 1], point)
            if idx == len(points) - 1:
                visited.add((point.x, point.y))


def update_position(head: Point2D, tail: Point2D) -> None:
    x_delta, y_delta = head.x - tail.x, head.y - tail.y
    if abs(x_delta) <= 1 and abs(y_delta) <= 1:
        return
    if abs(x_delta) > 1:
        tail_x = 0
        tail_y = 0
        if x_delta < 0:
            tail_x = -1
        else:
            tail_x = 1
        if y_delta > 0:
            tail_y = 1
        elif y_delta < 0:
            tail_y = -1
        tail.update_position(tail_x, tail_y)
    elif abs(y_delta) > 1:
        tail_x = 0
        tail_y = 0
        if y_delta < 0:
            tail_y = -1
        else:
            tail_y = 1
        if x_delta > 0:
            tail_x = 1
        elif x_delta < 0:
            tail_x = -1
        tail.update_position(tail_x, tail_y)


if __name__ == "__main__":
    main()
