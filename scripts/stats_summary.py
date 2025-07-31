import pandas as pd

df = pd.read_csv('data/syracuse_mbb_2023_core_stats.csv')

print("===== Summary Stats =====")
print(df.describe(include='all'))

print("\n===== Grouped by Player =====")
print(df.groupby('Player').agg(['sum', 'mean', 'max', 'min']))
