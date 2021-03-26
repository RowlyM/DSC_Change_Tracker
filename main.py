import pandas as pd
import data_sorting as ds



df = pd.read_csv('Data.csv')
plant = 'Refining West'

ds.sp_changes(df, plant)
