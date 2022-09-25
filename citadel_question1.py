def getTheGroups(n, operations, students1, students2):
    arr, res = [], []
    count = 0
    for i in range(len(operations)):
        if operations[i] == 'Total':
            a, b = students1[i], students2[i]
            for j in arr:
                if a in j:
                    count += len(j)
                if b in j:
                    count += len(j)
            res.append(count)
        if operations[i] == 'Friend':
            x, y = students1[i], students2[i]
            if len(arr) == 0:
                arr.append([x,y])
            else:
                for k in arr:
                    if x in k:
                        k.append(y)
                    elif y in k:
                        k.append(x)
    print(arr)
    return res
 
t = getTheGroups(4,['Friend', 'Friend', 'Total'], [1, 2, 1], [2, 3, 4])
print(t)

