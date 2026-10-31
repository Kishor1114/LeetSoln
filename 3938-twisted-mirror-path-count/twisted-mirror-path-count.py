class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9+7
        def get(r, c):
            return grid[r][c] if len(grid) > len(grid[0]) else grid[c][r]

        dp = [[0]*2 for _ in xrange(min(len(grid), len(grid[0]))+1)]
        dp[1] = [1]*2
        for r in xrange(max(len(grid), len(grid[0]))):
            for c in xrange(len(dp)-1):
                if get(r, c):
                    dp[c+1] = [dp[c+1][1], dp[c][0]]
                else:
                    dp[c+1] = [(dp[c+1][1]+dp[c][0])%MOD]*2
        return dp[-1][0]