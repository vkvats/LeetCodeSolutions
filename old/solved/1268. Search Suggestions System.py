class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        output = []
        for i in range(len(searchWord)):
            init = searchWord[:i + 1]
            sugg = []
            for word in products:
                if word.startswith(init):
                    sugg.append(word)
            if len(sugg) > 3:
                sugg = sugg[:3]
            output.append(sugg)
        return output

# Solution from leetcode
class SolutionF1:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # After sort, product list will follow alphabetic order
        products.sort()

        # Use two iter to hold the target words between
        start, end, ret = 0, len(products) - 1, []
        for n_th, c in enumerate(searchWord):
            # Check between start and end to prevent unusable move
            # Check lenth of current "product string" to prevent "search word" longer than "product string"
            while start <= end and (products[start][n_th] < c if len(products[start]) > n_th else True):
                start += 1
            while start <= end and (products[end][n_th] > c if len(products[end]) > n_th else True):
                end -= 1

            # Append at most three element array
            ret.append(products[start:start + 3] if end > start + 1 else products[start:end + 1])
        return ret

# Solution from leetcode
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        results = []

        search = ""
        startIndex = 0

        for s in searchWord:
            search = search + s
            # print(search,startIndex)
            suggest = []
            for i in range(startIndex, len(products)):
                p = products[i]
                if p.startswith(search):
                    suggest.append(p)
                    if len(suggest) == 1:
                        startIndex = i
                    if len(suggest) == 3:
                        break
            results.append(suggest)
            if len(suggest) == 0:
                while len(results) < len(searchWord):
                    results.append([])
                break

        return results

# using Bisect library
import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, i = [], '', 0
        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix, i)
            res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return res
