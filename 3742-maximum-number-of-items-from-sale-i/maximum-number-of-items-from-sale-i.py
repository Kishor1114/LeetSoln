class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        NEG_INF = float("-inf")
        cnt = [0]*(max(f for f, _ in items)+1)
        for f, _ in items:
            cnt[f] += 1
        total = [0]*len(cnt)
        for i in xrange(1, len(total)):
            if not cnt[i]:
                continue
            for j in xrange(i, len(total), i):
                total[i] += cnt[j]
        dp = [NEG_INF]*(budget+1)
        dp[0] = 0
        for f, p in items:
            for i in reversed(xrange(p, len(dp))):
                dp[i] = max(dp[i], dp[i-p]+total[f])
        min_p = min(p for _, p in items)
        return max(x+(budget-i)//min_p for i, x in enumerate(dp))