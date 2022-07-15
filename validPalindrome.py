class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = ''.join(filter(str.isalnum, s)).lower()
        if len(k) == 1:
            return True
        if list(k[:int(len(k)/2)]) == list(reversed(k[-1*int(len(k)/2):])):
            return True
        else:
            return False