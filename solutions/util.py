class Point2D:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def update_position(self, delta_x: int, delta_y: int) -> None:
        self.x += delta_x
        self.y += delta_y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def extract_numbers_from_string(s: str) -> list[int]:
    newstr = "".join((x if x in "0123456789" else " ") for x in s)
    return [int(i) for i in newstr.split()]


def extract_characters_from_string(s: str, chars: str) -> list[str]:
    newstr = "".join((x if x in chars else " ") for x in s)
    return newstr.split()
