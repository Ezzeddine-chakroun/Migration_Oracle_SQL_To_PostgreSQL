#from openpyxl import load_workbook
import os
import shutil
import pandas as pd

import numpy as np
path_to_tables = "All_Tables"
new_path = "New_Tables"
list_files = os.listdir(path_to_tables)
i=0
new_requests=[]
for file in list_files:
    i=i+1
    #In my case the extension is xlsx , you can change it if you use another xcel format
    new_name = file.split('.xlsx')[0]
    new_name = new_name+'.csv'
    read_file = pd.read_excel(os.path.join(path_to_tables,file))
    read_file=read_file.convert_dtypes()
    read_file.to_csv(os.path.join(new_path,new_name), index=None, header=True)
    print(str(i)+" is done")
