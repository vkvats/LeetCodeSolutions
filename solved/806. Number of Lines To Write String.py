class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        if not S: return [0, 0]
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {key: val for key, val in zip(alphabets, widths)}
        line_width = 0
        line_count = 1
        for char in S:
            w = alpha_dict[char]
            if line_width + w <= 100:
                line_width += w
            elif line_width + w > 100:
                line_count += 1
                line_width = w
        return [line_count, line_width]

# Solution from leetcode
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        t = 0
        lines = 0
        for c in s:
            w = widths[ord(c) - 97]
            t += w
            if t > 100:
                lines += 1
                t = w

        return [lines + 1, t]