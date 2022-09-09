class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = list(range(0,n+1))
        nums.sort()
        res = set(new_nums) - set(nums)
        return list(res)[0]