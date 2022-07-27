class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        hashmap = {}
        res = []
        for i in s:
            hashmap[i[-1]] = i[:-1]
        hashmap = collections.OrderedDict(hashmap)
        for keys in sorted(hashmap):
            res.append(hashmap[keys])
        return ' '.join(res)