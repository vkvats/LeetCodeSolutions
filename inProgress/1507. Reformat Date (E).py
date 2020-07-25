class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05",
                 "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        output = ""
        words = date.split()
        day = words[0]
        month = words[1]
        year = words[2]
        day = day[:-2]
        if len(day) ==1:
            day = "0" + day
        output = year + "-" + month_map[month] + "-" + day

# solution from leetcode
class SolutionF2:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(" ") # unpacking
        d = d[:len(d) - 2]
        if len(d) == 1:
            d = "0" + d

        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07",
                  "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}

        m = months[m]

        # print(d,m,y)
        res = y + "-" + m + "-" + d

        return res