import itertools
class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
        
        def lcm(a, b):
            return a//gcd(a, b)*b
        
        def check(target):
            return sum((-1 if (i+1)&1 else +1)*(target//l) for i in xrange(1, len(coins)+1) for l in lookup[i]) >= k

        def binary_search(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        lookup = [[] for _ in xrange(len(coins)+1)]
        for i in xrange(1, len(coins)+1):
            for comb in itertools.combinations(coins, i):
                lookup[i].append(reduce(lcm, comb))
        mn = min(coins)
        l = 1
        for i in xrange(1, 25+1):
            l = lcm(l, i)
        return binary_search(mn, k*mn, check)