# rock = A, paper = B, scissors = C
OPPONENT_INPUT: list[str] = ["A", "C", "B"]
CONVERSION = {"A": "X", "B": "Y", "C": "Z"}
INDEXES = {"A": 0, "C": 1, "B": 2}
SCORES = {"A": 1, "B": 2, "C": 3}


def main():
    part_1()
    part_2()


def part_1() -> None:
    score = 0
    with open("inputs/day2input.txt") as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            inputs = line.split(" ")
            opp_input = inputs[0]
            our_input = inputs[1].strip("\n")
            winning_input_idx = (INDEXES[opp_input] - 1) % len(OPPONENT_INPUT)
            drawing_input_idx = INDEXES[opp_input]
            losing_input_idx = (INDEXES[opp_input] + 1) % len(OPPONENT_INPUT)
            if CONVERSION[OPPONENT_INPUT[winning_input_idx]] == our_input:
                score += SCORES[OPPONENT_INPUT[winning_input_idx]] + 6
            elif CONVERSION[OPPONENT_INPUT[drawing_input_idx]] == our_input:
                score += SCORES[OPPONENT_INPUT[drawing_input_idx]] + 3
            else:
                score += SCORES[OPPONENT_INPUT[losing_input_idx]]
    print(score)


def part_2() -> None:
    score = 0
    with open("inputs/day2input.txt") as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            inputs = line.split(" ")
            opp_input = inputs[0]
            our_input = inputs[1].strip("\n")
            winning_input_idx = (INDEXES[opp_input] - 1) % len(OPPONENT_INPUT)
            drawing_input_idx = INDEXES[opp_input]
            losing_input_idx = (INDEXES[opp_input] + 1) % len(OPPONENT_INPUT)
            if our_input == "X":
                score += SCORES[OPPONENT_INPUT[losing_input_idx]]
            elif our_input == "Y":
                score += SCORES[OPPONENT_INPUT[drawing_input_idx]] + 3
            else:
                score += SCORES[OPPONENT_INPUT[winning_input_idx]] + 6
    print(score)


if __name__ == "__main__":
    main()
