class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = arr[0]
        for i in range(len(arr)):
            for j in range(1, len(arr)):
                if (len(arr[i:j+1]) % 2 != 0):
                    ans += sum(arr[i:j+1])
        return ans
                