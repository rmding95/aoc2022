def main():
    calories: list[int] = []
    with open("inputs/day1input.txt") as f:
        current_calories = 0
        for line in f.readlines():
            if line == "\n":
                calories.append(current_calories)
                current_calories = 0
                continue
            current_calories += int(line)
    calories_sorted = sorted(calories, reverse=True)
    print(sum(calories_sorted[0:3]))


if __name__ == "__main__":
    main()
