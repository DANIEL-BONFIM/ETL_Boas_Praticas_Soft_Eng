import pandas as pd
from typing import List

'''
Concatenate Function for combine all files

args: df_list: 

return pd.concat(df_list)

'''

def concat_files(df_list: List[pd.DataFrame]) -> pd.DataFrame:

  return pd.concat(df_list, ignore_index=True)


