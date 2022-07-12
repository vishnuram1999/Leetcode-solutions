def isValid(s):
    s = list(s)
    stacklist = []
    flag = True
    for i in range(len(s)):
        if(s[i] == "}" and "{" in stacklist):
            stacklist.remove("{")
        elif(s[i] == "]" and "[" in stacklist):
            stacklist.remove("[")
        elif(s[i] == ")" and "(" in stacklist):
            stacklist.remove("(")
        else:
            stacklist.append(s[i])
    if(stacklist):
        flag = False
    return flag


print(isValid("{[}]"))