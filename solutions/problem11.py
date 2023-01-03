from collections import deque

from util import extract_characters_from_string, extract_numbers_from_string

DIVISION_CONST = 3
ROUNDS = 10000


class Monkey:
    items: deque[int]
    operation_num: int
    is_multiplication_operator: bool
    is_addition_operator: bool
    is_square_operator: bool
    divisible_by: int
    if_true_monkey: int
    if_false_monkey: int
    inspected: int

    def __init__(self, starting_items: deque[int]):
        self.items = starting_items
        self.operation_num = 0
        self.is_multiplication_operator = False
        self.is_addition_operator = False
        self.is_square_operator = False
        self.divisible_by = 0
        self.if_true_monkey = 0
        self.if_false_monkey = 0
        self.inspected = 0

    def turn(self, divisor: int) -> int:
        item = self.items.popleft()
        if self.is_addition_operator:
            item += self.operation_num
        elif self.is_multiplication_operator:
            item *= self.operation_num
        else:
            item *= item
        item %= divisor
        self.inspected += 1
        return item

    def __repr__(self) -> str:
        return (
            f"items: {self.items}\n"
            f"operation num: {self.operation_num}\n"
            f"is *: {self.is_multiplication_operator}\n"
            f"is +: {self.is_addition_operator}\n"
            f"is ^2: {self.is_square_operator}\n"
            f"divisible by: {self.divisible_by}\n"
            f"if true monkey: {self.if_true_monkey}\n"
            f"if false monkey: {self.if_false_monkey}\n"
            f"inspect count: {self.inspected}\n"
        )


def main():
    monkeys: list[Monkey] = []
    with open("inputs/day11input.txt") as f:
        data = f.read().split("\n\n")
        for m in data:
            parse_monkeys(m, monkeys)
    divisor = 1
    for monkey in monkeys:
        divisor *= monkey.divisible_by
    for _ in range(ROUNDS):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                new_val = monkey.turn(divisor)
                if new_val % monkey.divisible_by == 0:
                    monkeys[monkey.if_true_monkey].items.append(new_val)
                else:
                    monkeys[monkey.if_false_monkey].items.append(new_val)
    top_2 = sorted(monkeys, key=lambda x: x.inspected, reverse=True)[:2]
    print(top_2[0].inspected * top_2[1].inspected)


def parse_monkeys(data: str, monkeys: list[Monkey]) -> None:
    lines = data.splitlines()
    starting_items = deque(extract_numbers_from_string(lines[1]))
    monkey = Monkey(starting_items)
    operator = extract_characters_from_string(lines[2], "+*")[0]
    operation_num = extract_numbers_from_string(lines[2])
    if operator == "+":
        monkey.is_addition_operator = True
    elif operator == "*":
        if len(operation_num) == 0:
            monkey.is_square_operator = True
        else:
            monkey.is_multiplication_operator = True
    if not monkey.is_square_operator:
        monkey.operation_num = operation_num[0]
    monkey.divisible_by = extract_numbers_from_string(lines[3])[0]
    monkey.if_true_monkey = extract_numbers_from_string(lines[4])[0]
    monkey.if_false_monkey = extract_numbers_from_string(lines[5])[0]
    monkeys.append(monkey)


if __name__ == "__main__":
    main()
