import pandas as pd
import os
from sqlalchemy import create_engine
import sqlalchemy as sa

path_to_tables = "New_Tous_Tables"
list_files = os.listdir(path_to_tables)
i=0
def creating_tables(dbschema,username,password,hostname,port):


    for file in list_files:
        i=i+1
        df = pd.read_csv(os.path.join(path_to_tables,file), low_memory=False)
        df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
        engine = create_engine('postgresql://'+username+':'+password+'@'+hostname+':'+str(port)+'/bdax040',
        connect_args={'options': '-csearch_path={}'.format(dbschema)})
        #print(file.split(".")[0])
        #insp = sa.inspect(engine)
        #db_list = insp.get_schema_names()
        #print(db_list)
        try:
            df.to_sql(file.split(".")[0], engine)
        except:
            print("Table already created")
            pass
        print("Done : "+str(i*100/len(list_files)))