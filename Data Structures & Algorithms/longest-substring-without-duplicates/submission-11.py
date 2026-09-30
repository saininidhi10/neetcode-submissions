class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_idx_map = {s[0]: 0}
        max_len = 0
        l, r = 0, 1

        while r < len(s):
            if s[r] in char_idx_map:
                if (char_idx_map[s[r]] + 1) > l and (char_idx_map[s[r]] + 1) <= r:
                    l = char_idx_map[s[r]] + 1
            max_len = max(max_len, r-l+1)
            char_idx_map[s[r]] = r
            r += 1
        
        return max_len