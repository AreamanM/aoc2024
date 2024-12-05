import collections
import functools
import itertools


f = open("inputs/day5.input")

type Rules = collections.defaultdict[int, set[str]]
type Updates = list[list[str]]
type Parsed = tuple[Rules, Updates]


def parse(f) -> Parsed:
    rules_section, updates_section = f.read().strip().split("\n\n")

    rules = collections.defaultdict(set)
    for rule in rules_section.split("\n"):
        before, after = rule.split("|")
        rules[before].add(after)

    updates = [[] for _ in updates_section.split("\n")]
    for i, update in enumerate(updates_section.split("\n")):
        for page in update.split(","):
            updates[i].append(page)

    return rules, updates


def part1(rules: Rules, updates: Updates) -> int:
    res = 0
    for update in updates:
        prev = set()
        for page_num in update:
            if prev.intersection(rules[page_num]):
                break
            prev.add(page_num)
        # else only runs when for loop isn't terminated early
        else:
            res += int(update[len(update) // 2])
    return res


def part2(rules: Rules, updates: Updates) -> int:
    res = 0
    for update in updates:
        prev = set()
        bad_pages = set()
        for page_num in update:
            # update is bad
            if prev.intersection(rules[page_num]):
                # element A > element B if B|A => A (is a member of) rules[B]
                update.sort(key=functools.cmp_to_key(
                                    lambda a, b:  1 if a in rules[b] else -1))
                res += int(update[len(update) // 2])
                break
            prev.add(page_num)
    return res

        
rules, updates = parse(f)
print(part1(rules, updates))
print(part2(rules, updates))

f.close()
