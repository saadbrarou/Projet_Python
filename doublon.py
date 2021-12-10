import pandas as pd

data = pd.read_excel ('pytest.xlsx')                                           # Read excel file
bdsid_col = pd.DataFrame(data, columns= ['Bdsid'])                             # Extract Bdsid column
bdsid_list=bdsid_col.values.tolist()                                           # Convert Bdsid to list from DataFrame
bdsid_list_o = [bdsid_list[i][0] for i in range(len(bdsid_list)) ]             # Change content of the list, from lists to element of these lists
bdsid_set_doublon = set([x for x in bdsid_list_o if bdsid_list_o.count(x) > 1])# To get duplicates elements
bdsid_list_doublon = list(bdsid_set_doublon)                                   # Convert from set to list : {} to []
techacces_col = pd.DataFrame(data, columns= ['Techno Acces'])                  # Extract Techno acces column
techacces_list =  techacces_col.values.tolist()                                # Convert Techno Acces to list from DataFrame
techacces_list_o = [techacces_list[i][0] for i in range(len(techacces_list)) ] # Change content of the list, from lists to element of these lists
row_index_to_delete = []                                                       # Define list of index to delete
for i in range(len(bdsid_list_doublon)):                                       # Determine element to delete
    ind = [j for j, val in enumerate(bdsid_list_o) if val == bdsid_list_doublon[i]] # Calculate indexes of each doublon in the column of Bdsid or Techno Acces (They are the same)
    doublon_tech_element = [techacces_list_o[y] for y in ind ]                 # Determine the techno access used for each index
    if 'fibre' in doublon_tech_element:                                        # If there is no 'fibre' we don't need to check anything
        row_index_to_delete_per_doublon = [ind[k] for k in range(len(doublon_tech_element)) if doublon_tech_element[k] == 'DSL' ]   # if the Techno access of the index is DSL, we append it's index in the list of index to delete
        if 'DSL' in doublon_tech_element :
            for l in range(len(row_index_to_delete_per_doublon)):
                row_index_to_delete.append(row_index_to_delete_per_doublon[l])

print(row_index_to_delete)

print("hello")
#row_index_to_delete = [row_index_to_delete[i][0] for i in range(len(row_index_to_delete)) ]


