class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1+nums2)
        mid = int(len(merged_list)/2)
        if (len(nums1) + len(nums2))%2 == 0:
            return (merged_list[mid]+merged_list[mid-1])/2
        else:
            return merged_list[mid]
        