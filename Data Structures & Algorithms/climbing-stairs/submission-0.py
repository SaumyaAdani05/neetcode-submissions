class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for k in range(n // 2 + 1):
            ans += math.comb(n - k, k)
        return ans