class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            list1 = []
            freq = nums[i]
            val = nums[i+1]
            for i in range(freq):
                list1.append(val)
            res = res + list1
        
        return res
        