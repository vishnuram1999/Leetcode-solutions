class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                flag = True
            hashmap[nums[i]] = i
        return flag  