l = [1, 2, 2, 3, 4, 4, 5, 3]
res = []
i=0
while i<(len(l)-1):
    if l[i]!=l[i+1]:
        res.append(l[i])
    elif l[i]==l[i+1]:
        i+=1
    i+=1
print(res)
