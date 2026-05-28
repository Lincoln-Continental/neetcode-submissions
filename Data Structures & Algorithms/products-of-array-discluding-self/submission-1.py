class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix_val = 1
        for i in range(len(nums)):
            prefix[i] = prefix_val 
            prefix_val *= nums[i]
        
        postfix_val = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix_val
            postfix_val *= nums[i]

        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]

        return res
        
    