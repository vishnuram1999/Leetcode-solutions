class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        list1 = s.split(":")
        res = []
        for i in range(ord(list1[0][0]), ord(list1[1][0]) + 1):
            for j in range(int(list1[0][1]), int(list1[1][1]) + 1):
                res.append(chr(i) + str(j)) 
        return res
        
        