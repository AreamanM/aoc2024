f = open("inputs/day2.input")


def parse(f) -> list[list[int]]:
    reports = []
    for report in f.read().splitlines():
        reports.append([int(lvl) for lvl in report.split()])
    return reports


def part1(reports: list[list[int]]) -> int:
    safe_count = 0
    for report in reports:
        safe_count += 1 if is_report_safe(report) else 0
    return safe_count


def part2(reports: list[list[int]]) -> int:
    safe_count = 0
    for report in reports:
        is_safe = is_report_safe(report)
        for i in range(len(report)):
            if is_report_safe(report[:i] + report[i + 1:]):
                is_safe = True
        safe_count += 1 if is_safe else 0
    return safe_count


def is_report_safe(report: list[int]) -> bool:
    assert len(report) > 1
    inc = report[1] - report[0] > 0
    safe = True
    for i in range(len(report) - 1):
        adj_diff = report[i + 1] - report[i]
        is_safe_lvl = (abs(adj_diff) > 0 and abs(adj_diff) < 4
                        and ((adj_diff > 0 and inc) or (adj_diff < 0 and not inc)))
        safe = is_safe_lvl and safe
    return safe

        
reports = parse(f)
print(part1(reports))
print(part2(reports))

f.close()
