class Solution(object):
    def findMissingElements(self, nums):
        lookup = set(nums)
        return [x for x in xrange(min(nums)+1, max(nums)) if x not in lookup]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        