class Solution(object):
    def minOperations(self, nums):
        def check(i, d):
            return all(nums[(i+j*d)%len(nums)] == j for j in xrange(len(nums)))

        idx = nums.index(0)
        return min(idx, 1+(len(nums)-idx)+1) if check(idx, +1) else min((idx+1)+1, 1+(len(nums)-(idx+1))) if check(idx, -1) else -1
        """
        :type nums: List[int]
        :rtype: int
        """
        