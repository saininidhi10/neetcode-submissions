class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        char_idx_map = {s[0]: 0}
        max_len = 0
        l, r = 0, 1

        while r < len(s):
            if s[r] in char_idx_map:
                new_idx = char_idx_map[s[r]] + 1
                if new_idx > l and new_idx <= r:
                    l = new_idx
            max_len = max(max_len, r-l+1)
            char_idx_map[s[r]] = r
            r += 1
        
        return max_len