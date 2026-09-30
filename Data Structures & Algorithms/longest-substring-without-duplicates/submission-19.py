class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_idx_map = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            if s[r] in char_idx_map:
                new_idx = char_idx_map[s[r]] + 1
                l = max(new_idx, l)
            max_len = max(max_len, r-l+1)
            char_idx_map[s[r]] = r
        
        return max_len