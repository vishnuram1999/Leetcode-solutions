def exist(board, word):
        count = 0
        for j in range(len(word)):
            for i in board:
                if word[j] in i:
                    count += 1
                    print(word[j])
                    j = j+1
                    
                    break
        
        return (True if count==len(word) else False)
        
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))