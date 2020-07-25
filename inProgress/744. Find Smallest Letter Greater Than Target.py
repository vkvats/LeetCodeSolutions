class Solution:
    def nextGreatestLetter(self, letters: [str], target: str) -> str:
        letters = sorted(list(set(letters)))

        left, right = 0, len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] == target:
                if mid == len(letters) - 1:
                    return letters[0]
                else:
                    return letters[mid + 1]
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left < len(letters):
            return letters[left]
        else:
            return letters[0]

# Solution from leetcode
class SolutionFast1:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     target_n = ord(target)-ord('a')
    #     for ch in letters:
    #         if ord(ch)-ord('a')>target_n:
    #             return ch
    #     return letters[0]

    # def nextGreatestLetter(self, letters, target):
    #     for letter in letters:
    #         if letter > target:
    #             return letter
    #     return letters[0] # If not found

    # # Using bisect:
    def nextGreatestLetter(self, letters, target):
        # bisect.bisect_right(letters, target) finds the index position
        # where you should insert the same elem (on the right side)
        # if its not found, returns the len(letters)

        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]

        # bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

        # An alternative question is when are they equivalent? By answering this, the answer to your question becomes clear.

        # They are equivalent when the the element to be inserted is not present in the list. Hence, they are not equivalent when the element to be inserted is in the list.

if __name__ == '__main__':
    letters = ["e","e","e","e","e","e","n","n","n","n"]
    target = "n"
    print(Solution().nextGreatestLetter(letters, target))