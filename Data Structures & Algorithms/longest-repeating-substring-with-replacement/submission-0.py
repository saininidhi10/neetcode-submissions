class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        max_len = 0
        char_array = [0]*26
        l = r = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            char_array[idx] += 1
            max_char_cnt = max(char_array)
            count = (r-l+1) - max_char_cnt

            while count > k and l < r:
                idx = ord(s[l]) - ord('A')
                char_array[idx] -= 1 
                l += 1
                count -= 1
            
            max_len = max(max_len, (r-l+1))
        
        return max_len      
