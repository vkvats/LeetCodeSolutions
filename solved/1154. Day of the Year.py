import calendar


class Solution:
    def dayOfYear(self, date: str) -> int:
        month_days = {"1": 31, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31,
                      "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
        year, month, day = date.split("-")
        day_count = 0
        if int(month) >= 2:
            for m in range(1, int(month)):
                if m == 2:
                    if calendar.isleap(int(year)):
                        day_count += 29
                    else:
                        day_count += 28
                else:
                    day_count += month_days[str(m)]
        day_count += int(day)
        return day_count

# solution from leetcode
class SolutionF1:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 400) == 0 or ((year % 4 == 0) and (year % 100 != 0)): days[1] = 29 # leap year condition
        return day + sum(days[:month-1])