class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[:int(len(s)/2)]
        b = s[int(len(s)/2):]
        count_a, count_b = 0, 0
        for i in range(len(a)):
            if a[i] in vowels:
                count_a += 1
            if b[i] in vowels:
                count_b += 1
        return count_a == count_b
        