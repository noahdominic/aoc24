def part1(file_as_per_line):
    reports = [line.split() for line in file_as_per_line]

    analyses = [report_is_safe_2(report) for report in reports]

    return analyses.count(True)

def part2(file_as_per_line):
    reports = [line.split() for line in file_as_per_line]

    analyses = [report_is_safe_2(report) or any([report_is_safe_2(report[:i] + report[i+1:]) for i in range(len(report))]) for report in reports]

    return analyses.count(True)



def report_is_safe_2(report):
    report_left = report[:(len(report) - 1)]
    report_right = report[1:]

    differences = [int(item[1]) - int(item[0]) for item in zip(report_left, report_right)]
    differences =  list(differences)

    differences_are_in_limits = not any( [difference > 3 or difference < -3 or difference == 0 for difference in differences] )

    positivenesses = [difference > 0 for difference in differences]
    positivenesses = list(positivenesses)

    differences_have_uniform_positiveness = all(positivenesses) or not any(positivenesses)

    return differences_are_in_limits and differences_have_uniform_positiveness
