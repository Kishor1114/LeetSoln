class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + stoneValue[i]
            
        # dp[i][j] stores the max score for subarray i...j
        dp = [[0] * n for _ in range(n)]
        
        # max_left[i][j] stores max(dp[i][k] + sum(i...k)) for k in range(i, j)
        max_left = [[0] * n for _ in range(n)]
        # max_right[i][j] stores max(dp[k][j] + sum(k...j)) for k in range(i+1, j+1)
        max_right = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Find the split point where left_sum >= right_sum
                while pref[mid+1] - pref[i] < pref[j+1] - pref[mid+1]:
                    mid += 1
                
                # If left_sum < right_sum, Bob throws away the right part.
                # We want to maximize left_sum + dp[i][k] for k in [i, mid-1]
                val1 = max_left[i][mid-1] if mid - 1 >= i else 0
                
                # If left_sum > right_sum, Bob throws away the left part.
                # We want to maximize right_sum + dp[k][j] for k in [mid+1, j]
                val2 = max_right[mid+1][j] if mid + 1 <= j else 0
                
                # If left_sum == right_sum, Alice can choose either side
                val3 = 0
                if pref[mid+1] - pref[i] == pref[j+1] - pref[mid+1]:
                    val3 = pref[mid+1] - pref[i] + max(dp[i][mid], dp[mid+1][j])
                
                dp[i][j] = max(val1, val2, val3)
                
                # Update our auxiliary arrays for the next lengths
                total_sum = pref[j+1] - pref[i]
                max_left[i][j] = max(max_left[i][j-1], dp[i][j] + total_sum)
                max_right[i][j] = max(max_right[i+1][j], dp[i][j] + total_sum)
                
        return dp[0][n-1]