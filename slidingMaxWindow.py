def maxSlidingWindow(nums, k):
    res = []
    i = 0
    while len(nums[i:i+k]) == k:
        res.append(max(nums[i:i+k]))
        i += 1
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))