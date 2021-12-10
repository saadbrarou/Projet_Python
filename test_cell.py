List = [['a'], [2], [3], ['a'], [3], [5], [3]]

set_list = set([x[0] for x in List if List.count(x[0]) > 1])
print(set_list)
# for i in range (1,len(List)) :
#     if List(i) not in Tablon :
#         Index_id_rep = []
#         find_rep = 0
#         if List[i][0] not in Tablon :
#             Index_id_rep = []
#             find_rep = 0
#             for j in range (i+1,len(List)) :
#                 if j != len(List):
#                     if List[i][0] == List[j][0] :
#                         find_rep = 1
#                         if List[i] not in List :
#                             Tablon[].append(List[i][0])


