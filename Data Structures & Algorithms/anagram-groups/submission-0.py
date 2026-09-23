class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        # if len(strs) == 1:
        #     return list(strs)
        
        char_str_map = defaultdict(list)
        for word in strs:
            cnt = [0]*26
            for s in word:
                cnt[ord(s) - ord('a')] += 1
            key = tuple(cnt)
            char_str_map[key].append(word)
        
        for _, val in char_str_map.items():
            result.append(val)
        
        return result