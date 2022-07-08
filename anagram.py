def isAnagram(s,t):
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

print(isAnagram('anagram', 'nagaram'))