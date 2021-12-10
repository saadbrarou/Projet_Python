# # # import pandas as pd
# # # import numpy as np
# # # exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# # #             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# # #             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# # #             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# # # labels =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# # # df = pd.DataFrame(exam_data, index = labels)
# # # print(df)
# # Liste  = [1, 2, 3, 3, 2, 4, 5]
# #
# # new_list = []
# # for i in Liste :
# #     if i not in new_list:
# #         new_list.append(i)
# #
# # print(new_list)
#
#
# import pandas as pd
#
# data = pd.read_excel ('pytest.xlsx')
# bdsid_col = pd.DataFrame(data, columns= ['Bdsid'])
# bdsid_list=bdsid_col.values.tolist()
# print(bdsid_list)
#
# table_doublon=[]
# for i in range(0,len(bdsid_list)):
#     index_per_id_rep = []
#     find_rep = 0
#
#
# #0xfd
# data = pd.read_excel ('pytest.xlsx')
# duplicates = data.groupby()
#
# bdsidList = duplicates.filter['bdsid']
# bdsdListNoDuplicates = bdsidList.drop_duplicates
#
# lines = data.query('bdsid in @bdsdListNoDuplicates and techno = "fibre"')
#
# data[lines[bdsid]]#liste des bdsid qui ont une techno fibre
#
# mask = data['techno'] == 'fibre'
# #data.loc[mask, ]



# import csv
# file = open("C:\Users\u249467\Desktop\fichier1.csv)
# csvreader = csv.reader(file)
# for row in csvreader :
# print(row)

import pandas as pd
fichier1 = pd.read_csv("C:/Users/u249467/Desktop/fichier1.csv", sep = ';')
print(fichier1)
