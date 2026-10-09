class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        prev_s, prev_e = intervals[0]

        for curr_s, curr_e in intervals[1:]:
            if prev_s <= curr_s <= prev_e:
                prev_e = max(prev_e, curr_e)
            else:
                result.append([prev_s, prev_e])
                prev_s, prev_e = curr_s, curr_e

        result.append([prev_s, prev_e])
        return result