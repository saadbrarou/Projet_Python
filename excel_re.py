import pandas as pd
import numpy as np

data = pd.read_excel ('pytest.xlsx')
duplicates = data.groupby()['List']

bdsidList = duplicates.filter['bdsid']
bdsdListNoDuplicates = bdsidList.drop_duplicates

lines = data.query('bdsid in @bdsdListNoDuplicates and techno = "fibre"')

data[lines[bdsid]]#liste des bdsid qui ont une techno fibre

mask = data['techno'] == 'fibre'
#data.loc[mask, ]