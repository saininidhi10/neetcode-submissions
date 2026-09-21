from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        max_len = -1
        char_map = defaultdict(int)

        while j < len(s):
            if s[j] in char_map:
                max_len = max(max_len, j-i)
                new_i = char_map[s[j]] + 1
                if i < new_i:
                    i = new_i
                
            char_map[s[j]] = j
            j += 1

        return max(max_len, j-i)
