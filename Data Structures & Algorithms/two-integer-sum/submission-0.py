class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx_map = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_idx_map:
                return [num_idx_map[complement], idx]
            num_idx_map[num] = idx
        
        return []