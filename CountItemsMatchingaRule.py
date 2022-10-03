class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        hashmap = {"type": 0, "color": 1, "name": 2}
        
        for i in items:
            if ruleValue == i[hashmap[ruleKey]]:
                res += 1
        return res