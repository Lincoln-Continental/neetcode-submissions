class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        prefix_value = 1
        for i in range(len(nums)):
            prefix[i] = prefix_value
            prefix_value *= nums[i]

        postfix_value = 1
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = postfix_value
            postfix_value *= nums[i] 

        for i in range(len(result)):
            result[i] = prefix[i] * postfix[i]

        return result