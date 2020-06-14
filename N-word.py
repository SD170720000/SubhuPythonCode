# (3.) You are given n-words. Some words may repeat. For each word, output its number of               occurrences. The output order should correspond with the input order of the            appearance of the word. See the sample input/output for clarification. 
#Constraints 
#1<_n<_10​5 The sum of the lengths of all the words do not exceed ​ 10​6 All the words are composed of lowercase English letters only. 


n  = int(input())

mySet = set()
myDict = {}

for i in range(n):
    inp = input()[:-1]
    if inp not in mySet:
        mySet.add(inp)
        myDict[inp] = 1
    else:
        myDict[inp] += 1

print(len(mySet))
# print(' '.join(list(map(str, myDict.values()))))
print(*myDict.values())
