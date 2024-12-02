f = open("inputs/day1.input")


def parse(f) -> tuple[list, list]:
    left, right = [], []
    for line in f.read().splitlines():
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left.sort()
    right.sort()

    return left, right


def part1(left: list[int], right: list[int]):
    left.sort()
    right.sort()

    dist = 0

    for l, r in zip(left, right):
        dist += abs(l - r)
    return dist


def part2(left: list[int], right: list[int]):
    sim_score = 0 
    counts = {}
    for n in right:
        counts[n] = counts.get(n, 0) + 1
    for n in left:
        sim_score += counts.get(n, 0) * n
    return sim_score



left, right = parse(f)
print(part1(left, right))
print(part2(left, right))

f.close()
