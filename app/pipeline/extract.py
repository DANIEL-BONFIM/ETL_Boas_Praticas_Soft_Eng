import os #manipulate files/folders
import glob #list files

import pandas as pd 

from typing import List
'''
Function for read files in a folder data/input and return a dataframe list 

args: input_path (str): folder path

return: dataframe list

'''

def extract_from_excel(input_path: str) -> List[pd.DataFrame]:
  
  path = input_path
  all_files = glob.glob(os.path.join(input_path, "*.xls"))

  
  df_list = []
  for file in all_files:
    df_list.append(pd.read_excel(file, engine='xlrd'))

  
  return df_list


if __name__ =="__main__":
  
  in_path = 'data/Input'
  
  df_list= extract_from_excel(input_path = in_path )
  print(df_list)
  
