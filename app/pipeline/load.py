import pandas as pd 
import os

'''

load function of concatenated data

args: 
  
  dataframes (dataframe),

  outputpath (str): folder for load 

  file_name (str): name of file result from function
'''
  
def load_data(dataframes: pd.DataFrame, outputpaht: str, file_name: str)-> str:
  
  if not os.path.exists(outputpaht):
    os.mkdir(outputpaht)
  
  dataframes.to_excel(f'{outputpaht}/{file_name}.xlsx', index=False)

  return print('Congrats, all files has been concatenated')