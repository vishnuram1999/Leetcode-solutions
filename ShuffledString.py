class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_string=''
        for i in range(len(indices)):
            index = indices.index(i)
            shuffled_string += s[index]
        return shuffled_string
            