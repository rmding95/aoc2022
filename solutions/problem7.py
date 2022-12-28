from typing import Optional


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __repr__(self) -> str:
        return f"name: {self.name}, size: {self.size}"


class Directory:
    name: str
    parent: Optional["Directory"]
    files: list[File]
    subdirs: list["Directory"]

    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.files = []
        self.subdirs = []

    def __repr__(self) -> str:
        return f"{self.name}, parent: {self.parent}, files: {self.files}, subdirs: {self.subdirs}"


class Filesystem:
    root: str
    cwd: Directory

    def __init__(self, root: Directory):
        self.root = root
        self.cwd = root

    def get_current_dir(self) -> Directory:
        return self.cwd

    def create_dir(self, new_dir: str) -> None:
        if new_dir in self.cwd.subdirs:
            raise Exception(f"{new_dir} already exists in {self.cwd}'s subdirs")
        new_d = Directory(new_dir)
        new_d.parent = self.cwd
        self.cwd.subdirs.append(new_d)

    def get_parent(self, cwd: str) -> str:
        parent = self.cwd.parent
        if parent is None:
            raise Exception(f"{cwd} has no parent")
        return parent

    def create_file(self, file_size: int, file_name: str) -> None:
        file = File(file_name, file_size)
        self.cwd.files.append(file)

    def cd(self, new_dir: str) -> None:
        if new_dir == "/":
            self.cwd = self.root
            return
        for subdir in self.cwd.subdirs:
            if new_dir == subdir.name:
                self.cwd = subdir
                return
        raise Exception(
            f"{new_dir} not a subdir of {self.cwd}, subdirs: {self.cwd.subdirs}"
        )

    def ls(self, instructions: list[str], i: int) -> None:
        idx = i + 1
        while idx < len(instructions) and instructions[idx][0] != "$":
            instruction = instructions[idx].strip("\n")
            parts = instruction.split(" ")
            if parts[0] == "dir":
                self.create_dir(parts[1])
            else:
                self.create_file(int(parts[0]), parts[1])
            idx += 1

    def get_dir_sizes(self) -> dict[Directory, int]:
        sizes: dict[Directory, int] = {}
        current_dir = self.root
        self._get_size_helper(sizes, current_dir)
        return sizes

    def _get_size_helper(
        self, sizes: dict[Directory, int], current_dir: Directory
    ) -> int:
        size = 0
        for subdir in current_dir.subdirs:
            size += self._get_size_helper(sizes, subdir)
        for file in current_dir.files:
            size += int(file.size)
        sizes[current_dir] = size
        return size

    def __repr__(self) -> str:
        sizes = self.get_dir_sizes()
        s = ""
        for d, size in sizes.items():
            s += f"{d}\nsize: {size}\n"
        return s


TOTAL_DISK_SPACE = 70000000
REQUIRED_FREE_DISK_SPACE = 30000000


def main():
    root = Directory("/")
    filesystem = Filesystem(root)
    with open("inputs/day7input.txt") as f:
        instructions = f.readlines()
        i = 0
        while i < len(instructions):
            instruction = instructions[i].strip("\n")
            if len(instruction) == 0 or instruction[0] != "$":
                i += 1
                continue
            parts = instruction.split(" ")
            if parts[1] == "cd":
                if parts[2] == "..":
                    filesystem.cwd = filesystem.get_parent(filesystem.cwd)
                else:
                    filesystem.cd(parts[2])
            else:
                filesystem.ls(instructions, i)
            i += 1
    dir_sizes = filesystem.get_dir_sizes()
    # part 1 answer
    ans = 0
    for dir_size in dir_sizes.values():
        if dir_size <= 100000:
            ans += dir_size
    print(ans)
    # part 2 answer
    total_size = dir_sizes[root]
    free_space = TOTAL_DISK_SPACE - total_size
    space_needed = REQUIRED_FREE_DISK_SPACE - free_space
    sizes = dir_sizes.values()
    print(min([x for x in sizes if x > space_needed]))


if __name__ == "__main__":
    main()
