class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        max_len = 0
        char_cnt = defaultdict(int)
        l = 0
        maxf = 0

        for r in range(len(s)):
            char_cnt[s[r]] += 1
            maxf = max(maxf, char_cnt[s[r]])
            count = (r-l+1) - maxf

            while count > k:
                char_cnt[s[l]] -= 1 
                l += 1
                count -= 1
            
            max_len = max(max_len, (r-l+1))
        
        return max_len      
