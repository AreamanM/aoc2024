import functools
import operator
import re


f = open("inputs/day3.input")


def parse(f) -> str:
    # not much parsing to do today
    return f.read()


def part1(mem: str) -> int:
    muls = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    total = 0
    for match in muls.finditer(mem):
        total += int(match.group(1)) * int(match.group(2))
    return total


def part2(mem: str) -> int:
    # giga because this giga regular expression matches everything I need
    giga = re.compile(r"don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\)")

    total = 0
    do_mul = True
    for m in giga.finditer(mem):
        if do_mul and m.group(0).startswith("mul"):
            total += int(m.group(1)) * int(m.group(2))
        elif m.group(0) == "do()":
            do_mul = True
        else:
            do_mul = False
    return total


mem = parse(f)
print(part1(mem))
print(part2(mem))

f.close()
