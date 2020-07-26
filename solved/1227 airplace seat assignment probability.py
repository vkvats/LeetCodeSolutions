class Solution:
    '''
    Idea A. Induction:
            1 => 1
            2 => 1/2
            3 => 1/3 + 1/3 * 1/2 = 3/6 = 1/2
            4 => 1/4 + 3/4 * 1/3 = 2/4 = 1/2
    '''
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n < 2:
            return 1.0
        return 0.5