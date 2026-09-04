class Solution(object):
    def firstStableIndex(self, nums, k):
        right = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            right[i] = min(right[i+1], nums[i])
        left = 0
        for i in xrange(len(nums)):
            left = max(left, nums[i])
            if left-right[i] <= k:
                return i
        return -1
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        