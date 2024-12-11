def is_safe_report(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)):
        return False
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if not 1 <= diff <= 3:
            return False
    return True


reports = []

with open("input") as f:
    for line in f:
        r = []
        for value in line.split():
            r.append(int(value))
        reports.append(r)

print(sum(is_safe_report(report) for report in reports))
