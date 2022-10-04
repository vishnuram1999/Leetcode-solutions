class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res, list1 = [], []
        hashmap = {}        
        
        for i in range(len(groupSizes)):
            if groupSizes[i] in hashmap:
                hashmap[groupSizes[i]].append(i)
            else:
                hashmap[groupSizes[i]] = [i]
        for keys, values in hashmap.items():
            if len(values) == keys:
                res.append(values)
            else:
                start = 0
                flag = 1
                while(flag==1):
                    end = keys+start
                    res.append(values[start:end])
                    start = end
                    if(end == len(values)):
                        flag =0
                
        print(hashmap)
        return res
            
        