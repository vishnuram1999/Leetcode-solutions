class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        dict1 = dict()
        res = []
        for i in range(len(score)):
            dict1[score[i][k]] = score[i]
        while(len(dict1) > 0):
            res.append(dict1[max(dict1)])
            del dict1[max(dict1)]
        return res