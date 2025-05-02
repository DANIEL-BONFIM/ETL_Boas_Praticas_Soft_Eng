from pipeline.extract import extract_from_excel
from pipeline.transform import concat_files
from pipeline.load import load_data

if __name__ == '__main__':
  df_list = extract_from_excel('data/input')
  df = concat_files(df_list)
  load_data(df, 'data/output', 'output')


