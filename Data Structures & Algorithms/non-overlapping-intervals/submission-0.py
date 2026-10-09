class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        k = float("-inf")
        intervals.sort(key = lambda x: x[1])

        for x, y in intervals:
            if x >= k:
                k = y
            else:
                ans += 1
        
        return ans