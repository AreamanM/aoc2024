f = open("inputs/day4.input")


LEFT, RIGHT = 1, 2
UP, DOWN = 3, 4
TR, TL = 5, 6
BR, BL = 7, 8

OFFSETS = {
    LEFT: (-1, 0), RIGHT: (1, 0),
    UP: (0, -1), DOWN: (0, 1),
    TL: (-1, -1), TR: (1, -1),
    BL: (-1, 1), BR: (1, 1)
}


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
            for d in OFFSETS:
                if search(board, (x + OFFSETS[d][0],
                          y + OFFSETS[d][1]), "MAS", d):
                    instances += 1
    return instances


def part2(board: dict[tuple[int, int], str]) -> int:
    instances = 0
    for x, y in board:
        if board[(x, y)] == "A":
            mas_counts = 0
            dirs = [BL, BR, TL, TR]
            for i, d in enumerate(dirs):
                # len(dirs) - 1 = 3
                if search(board, (x + OFFSETS[d][0], y + OFFSETS[d][1]), "MAS", dirs[3 - i]):
                    mas_counts += 1
            if mas_counts == 2:
                instances += 1
    return instances


def search(
        b: dict[tuple[int, int], str], c: tuple[int, int],
        l: str, d: int) -> bool:
    if b.get(c, "-") == l[0]:
        return search(
                b, (c[0] + OFFSETS[d][0],
                c[1] + OFFSETS[d][1]), l[1:], d) if len(l) > 1 else True


board = parse(f)
print(part1(board))
print(part2(board))

f.close()
