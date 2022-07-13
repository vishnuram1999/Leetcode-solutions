class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        arr1 = nums[:int(len(nums)/2)]
        arr2 = nums[int(len(nums)/2):]
        for i in range(len(arr1)):
            res.append(arr1[i])
            res.append(arr2[i])
        return res