class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = dict()
        countt = dict()
        for c in s:
            counts[c] = counts.get(c,0) + 1
        for c in t:
            countt[c] = countt.get(c,0) + 1
        if(counts == countt):
            return True
        else:
            return False