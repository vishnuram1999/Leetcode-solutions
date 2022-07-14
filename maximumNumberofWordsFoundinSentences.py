class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxlength = 0
        for i in sentences:
            res = i.split(' ')
            length = len(res)
            if length > maxlength:
                maxlength = length
        return maxlength