import pandas as pd

data = pd.read_excel ('pytest.xlsx')
bdsid_col = pd.DataFrame(data, columns= ['Bdsid'])

#print(data.head(2))
bdsid_list=bdsid_col.values.tolist()
table_doublon=[]
for i in range(0,len(bdsid_list)):
    index_per_id_rep = []
    find_rep = 0
    if bdsid_list[i][0] not in table_doublon:
        for j in range(i+1,len(bdsid_list)):
            if j !=len(bdsid_list):
                    if bdsid_list[i][0] == bdsid_list[j][0]:
                        find_rep=1
                        if bdsid_list[i][0] not in table_doublon:
                            table_doublon.append(bdsid_list[i][0])
                            index_per_id_rep.append(i)
                        index_per_id_rep.append(j)
        if find_rep:
            table_doublon.append(index_per_id_rep)

print(table_doublon)

techacces_col = pd.DataFrame(data, columns= ['Techno Acces'])
techacces_list =  techacces_col.values.tolist()
print(techacces_list[2][0])
#print(techacces_list)
row_index_to_delete = []

for i_del in range(0,len(table_doublon),2):
    index_i = table_doublon[i_del+1]
    b = [techacces_list[id] for id in range(0, len(techacces_list)+1) if techacces_list.index(techacces_list[id]) in index_i and id in index_i]
    print(b)
# j_del_1 = 0
# j_del_2 = 0
# for i_del in range(0,len(table_doublon)):
#     fibre_exist = 0
#     dsl_exist = 0
#     while index_rep[j_del_1] != 'end':
#         if techacces_list[index_rep[j_del_1]][0] == 'fibre':
#             fibre_exist = 1
#         j_del_1 = j_del_1 + 1
#     j_del_1 =  j_del_1 +1
#
#     if fibre_exist:
#         while index_rep[j_del_2] != 'end':
#             if techacces_list[index_rep[j_del_2]][0] == 'DSL':
#                 row_index_to_delete.append(index_rep[j_del_2] +2)
#             j_del_2 = j_del_2 + 1
#         j_del_2 = j_del_2 + 1
#     else:
#         j_del_2 = j_del_1
#
# print(row_index_to_delete)

#    index_start=0
#    for j in range(index_start,len(index_rep):
#        fibre_exist = 0
#        if b[j][0] == 'fibre':
#            fibre_exist =1
#        if b[j][0] == 'end':
#            index_start = j+1



#import library
