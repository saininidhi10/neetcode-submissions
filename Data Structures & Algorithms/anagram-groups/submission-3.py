class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        char_str_map = defaultdict(list)
        for word in strs:
            cnt = [0]*26
            for s in word:
                cnt[ord(s) - ord('a')] += 1
            key = tuple(cnt)
            char_str_map[key].append(word)
        
        return list(char_str_map.values())