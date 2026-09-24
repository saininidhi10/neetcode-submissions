class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        zero_cnt = 0
        prod = 1

        for i, num in enumerate(nums):
            if num == 0:
                zero_cnt += 1
            else:
                prod *= num
            res[i] = prod
        
        if zero_cnt > 1: return [0]*len(nums)

        for i, num in enumerate(nums):
            if zero_cnt:
                res[i] = 0 if num else prod
            else:
                res[i] = prod // num
        
        return res