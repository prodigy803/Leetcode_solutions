class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums,reverse=True)
        current_result = []
        
        if len(nums) == 1:
            return nums
        else:
            for i in range(len(nums)):
                if sum(sorted_nums[:i]) > sum(sorted_nums[i:]):
                    current_result = sorted_nums[:i].copy()
                    break
                if i == len(nums) - 1:
                    current_result = nums

            return current_result
        