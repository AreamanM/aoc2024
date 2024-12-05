f = open("inputs/day4.input")


def parse(f) -> dict[tuple[int, int], str]:
    board = {}
    for y, line in enumerate(f.read().splitlines()):
        for x, char in enumerate(line):
            board[(x, y)] = char
    return board


def part1(board: dict[tuple[int, int], str]) -> int:
    instances = 0
    for x, y in board:
        if board[(x, y)] == "X":
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if search(board, (x + i, y + j), (i, j), "MAS"):
                        instances += 1
    return instances


def part2(board: dict[tuple[int, int], str]) -> int:
    instances = 0
    for x, y in board:
        if board[(x, y)] == "A":
            mas_counts = 0
            for i in [-1, 1]:
                for j in [-1, 1]:
                    if search(board, (x + i, y + j), (-i, -j), "MAS"):
                        mas_counts += 1
            if mas_counts == 2:
                instances += 1
    return instances


def search(
        b: dict[tuple[int, int], str], c: tuple[int, int],
        d: tuple[int, int], l: str) -> bool:
    if b.get(c, "-") == l[0]:
        return search(
                b, (c[0] + d[0], c[1] + d[1]), d, l[1:]) if len(l) > 1 else True


board = parse(f)
print(part1(board))
print(part2(board))

f.close()
