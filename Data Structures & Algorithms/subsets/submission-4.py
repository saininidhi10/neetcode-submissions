class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Cascading: TC = O(N*2^N); SC = O(N*2^N)
        # output = [[]]

        # for num in nums:
        #     newSubsets = []
        #     for curr in output:
        #         temp = curr.copy()
        #         temp.append(num)
        #         newSubsets.append(temp)
        #     for curr in newSubsets:
        #         output.append(curr)
        
        # return output

        #Backtracking: TC = O(N*2^N), SC = O(N)
        # def backtrack(first, curr, nums):
        #     output.append(curr[:])

        #     for i in range(first, n):
        #         curr.append(nums[i])
        #         backtrack(i+1, curr, nums)
        #         curr.pop()
        
        # output = []
        # n = len(nums)
        # backtrack(0, [], nums)
        # return output

        #Bitmask TC = O(N*2^N), SC = O(N)
        n = len(nums)
        output = []

        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            # print(bitmask)
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
            # print(output)
        
        return output