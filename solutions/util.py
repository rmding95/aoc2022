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


# def print_points_2D(points: list[tuple[int, int]]) -> None:
#     max_x = max([x[0] for x in points])
#     max_y = max([x[1] for x in points])
#     arr: list[list[int]] = []
#     for _ in range(max_y):
#         arr.append([0] * max_x)
#     for point in points:
#         arr[point[0]][point[1]] = 1
