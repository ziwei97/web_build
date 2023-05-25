

a=[[1,2,3,4],["a","b","c","d"],["a","b","c","d"]]



result=[]
temp = {}

for i in a:
    temp["id"]= i[0]
    temp["gender"]=i[1]
    temp["salary"]=i[2]
    print(temp)
    result.append(temp.copy())

print(result)