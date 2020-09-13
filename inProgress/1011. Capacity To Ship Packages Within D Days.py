class Solution:
    def shipWithinDays(self, weights: [int], D: int) -> int:
        # Binary search
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi)//2
            day= 1
            weight_sum = 0
            for w in weights:
                weight_sum += w
                # if weight_sum == mid:
                #     weight_sum = 0
                #     day += 1
                if weight_sum > mid:
                    weight_sum = w
                    day += 1
            # if weight_sum != 0: day += 1
            if day > D:
                lo = mid + 1
            else:
                hi = mid
        return lo

# compacted version of above code
class Solution:
    def shipWithinDays(self, weights: [int], D: int) -> int:
        # Binary search
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi)//2
            day= 1
            weight_sum = 0
            for w in weights:
                weight_sum += w
                if weight_sum > mid:
                    weight_sum = w
                    day += 1
            if day > D:
                lo = mid + 1
            else:
                hi = mid
        return lo

# More organized version of same code,
# its good practice to separate condition check
# and write it as separate function
def shipWithinDays(weights: [int], D: int) -> int:
    # Condition check
    def feasible(capacity) -> bool:
        days = 1
        total = 0
        for weight in weights:
            total += weight
            if total > capacity:  # too heavy, wait for the next day
                total = weight
                days += 1
                if days > D:  # cannot ship within D days
                    return False
        return True
    # binary search in search space.
    left, right = max(weights), sum(weights)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid): # Condition check
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    w = [1,2,3,1,1]
    d = 4
    print(Solution().shipWithinDays(w, d))