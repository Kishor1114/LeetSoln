MOD = 10**9+7
MAX_N = 1000
fact = [0]*(2*MAX_N-1+1)
inv = [0]*(2*MAX_N-1+1)
inv_fact = [0]*(2*MAX_N-1+1)
fact[0] = inv_fact[0] = fact[1] = inv_fact[1] = inv[1] = 1
for i in xrange(2, len(fact)):
    fact[i] = fact[i-1]*i % MOD
    inv[i] = inv[MOD%i]*(MOD-MOD//i) % MOD
    inv_fact[i] = inv_fact[i-1]*inv[i] % MOD

class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def nCr(n, k, mod):
            return (fact[n]*inv_fact[n-k] % mod) * inv_fact[k] % mod
        return nCr(n+k-1, 2*k, MOD)