import collections
class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count = collections.Counter(stone % 3 for stone in stones)
        
        # Scenario 1: Even number of remainder 0 stones
        if count[0] % 2 == 0:
            return min(count[1], count[2]) > 0
            
        # Scenario 2: Odd number of remainder 0 stones
        return abs(count[1] - count[2]) > 2