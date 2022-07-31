class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return (True if x[::-1] == x else False)