a = [['a'], [2], [3], ['a'], [3], [5], [3]]
T=[]
for i in range(0,len(a)):
    #find_rep = 0
    if a[i][0] not in T:
        index_per_id_rep = []
        find_rep = 0
        for j in range(i+1,len(a)):
            if j !=len(a):
                    if a[i][0] == a[j][0]:
                        find_rep=1
                        if a[i][0] not in T:
                            T.append(a[i][0])
                            index_per_id_rep.append(i)
                        index_per_id_rep.append(j)
        if find_rep:
            T.append(index_per_id_rep)


print(T)
