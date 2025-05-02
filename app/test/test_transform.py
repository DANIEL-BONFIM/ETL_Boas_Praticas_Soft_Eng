import pandas as pd 
from app.pipeline.transform import concat_files

'''
testing function for validate the concatenation of xls files
'''
df1 = pd.DataFrame({'col1': [4, 5], 'col2': [1, 2]})
df2 = pd.DataFrame({'col1': [6, 9], 'col2': [1, 2]})


def testing_concat():

  # arrange
  dataframe_test = pd.concat([df1,df2], ignore_index=True)

  # act
  df = concat_files([df1,df2])  # because is a list of df

  # assert
  assert df.shape == (4,2)
  assert dataframe_test.equals(df)
  