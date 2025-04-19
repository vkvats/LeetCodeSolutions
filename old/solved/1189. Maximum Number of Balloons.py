# new solution
# using counter and min(division of target words)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        b = Counter("balloon")
        return min(count[char]//b[char] for char in "balloon")

def maxNumberOfBalloons(text):
    count = {}
    num_of_balloon =0
    for alpha in text:
        count[alpha] = count.get(alpha,0) +1
    while True:
        for alpha2 in "balloon":
            if alpha2 in count:
                count[alpha2] -=1
                if count[alpha2] ==-1:
                    return num_of_balloon
            else:
                return num_of_balloon
        num_of_balloon +=1

# best solution on leetcode
from collections import Counter
def maxNumberOfBalloonsBest(text):
    counter = Counter(text)
    b = counter['b']
    a = counter['a']
    l = counter['l'] // 2
    o = counter['o'] // 2
    n = counter['n']
    return min(b, a, l, o, n)

if __name__ == '__main__':
    text = "nlaebolko"
    text = "loonbalxballpoon"
    text = "lloo"
    print(maxNumberOfBalloons(text))