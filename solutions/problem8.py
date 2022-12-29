def main():
    trees: list[list[int]] = []
    seen: set[tuple[int, int]] = set()
    with open("inputs/day8input.txt") as f:
        data = f.read().splitlines()
        for line in data:
            trees.append([int(x) for x in list(line)])
    # part 1
    print(find_visible_trees(trees, seen))
    # part 2
    max_visibility = 0
    for row, col in seen:
        max_visibility = max(get_visibility_score(row, col, trees), max_visibility)
    print(max_visibility)


def find_visible_trees(trees: list[list[int]], seen: set[tuple[int, int]]) -> int:
    for i in range(len(trees)):
        seen.add((0, i))
        seen.add((len(trees) - 1, i))
        seen.add((i, 0))
        seen.add((i, len(trees) - 1))
    # looking left
    for row in range(len(trees)):
        current_max = trees[row][0]
        for col in range(len(trees)):
            if trees[row][col] > current_max:
                current_max = trees[row][col]
                if (row, col) in seen:
                    continue
                seen.add((row, col))
    # looking from above
    for col in range(len(trees)):
        current_max = trees[0][col]
        for row in range(len(trees)):
            if trees[row][col] > current_max:
                current_max = trees[row][col]
                if (row, col) in seen:
                    continue
                seen.add((row, col))
    # looking right
    for row in range(len(trees)):
        current_max = trees[row][len(trees) - 1]
        for col in range(len(trees) - 1, -1, -1):
            if trees[row][col] > current_max:
                current_max = trees[row][col]
                if (row, col) in seen:
                    continue
                seen.add((row, col))
    # looking from below
    for col in range(len(trees)):
        current_max = trees[len(trees) - 1][col]
        for row in range(len(trees) - 1, -1, -1):
            if trees[row][col] > current_max:
                current_max = trees[row][col]
                if (row, col) in seen:
                    continue
                seen.add((row, col))
    return len(seen)


def get_visibility_score(row: int, col: int, trees: list[list[int]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
    score = 1
    for direction in directions:
        current_max = trees[row][col]
        steps = 0
        tmp_row = row
        tmp_col = col
        while True:
            tmp_row += direction[0]
            tmp_col += direction[1]
            next_step = (tmp_row, tmp_col)
            if (
                next_step[0] >= len(trees)
                or next_step[0] < 0
                or next_step[1] >= len(trees)
                or next_step[1] < 0
            ):
                score *= steps
                break
            steps += 1
            if trees[next_step[0]][next_step[1]] >= current_max:
                score *= steps
                break
    return score


if __name__ == "__main__":
    main()
