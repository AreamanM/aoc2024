import functools
import operator
import re


f = open("inputs/day3.input")


def parse(f) -> str:
    # not much parsing to do today
    return f.read()


def part1(mem: str) -> int:
    muls = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    nums = re.compile(r"\d{1,3}")

    total = 0
    for match in muls.findall(mem):
        total += functools.reduce(operator.mul, map(int, nums.findall(match)))
    return total


def part2(mem: str) -> int:
    # giga because this giga regular expression matches everything I need
    giga = re.compile(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)")
    nums = re.compile(r"\d{1,3}")

    total = 0
    do_mul = True
    for m in giga.findall(mem):
        if do_mul and m.startswith("mul"):
            total += functools.reduce(operator.mul, map(int, nums.findall(m)))
        elif m == "do()":
            do_mul = True
        else:
            do_mul = False
    return total


mem = parse(f)
print(part1(mem))
print(part2(mem))

f.close()
