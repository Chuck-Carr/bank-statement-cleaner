import pandas as pd
import numpy as np
import re

pattern = re.compile(r"[/.]")

import_file = "Files/Checking_January.csv"
export = pattern.split(import_file)[1]
export_file = "Files/" + export + f"{'_cleaned'}.csv"

df = pd.read_csv(import_file, sep=",", usecols=['Date','Transaction','Name','Amount'])
df = df.rename(columns={'Transaction':'Type','Name':'Details'})
df['Amount'] = abs(df['Amount'])
df = df.replace(['CREDIT'], 'Income')
df = df.replace(['DEBIT'], 'Expenses')
df['Type'] = np.where(df['Type'].isin(['Income', 'Expenses']), df['Type'], 'Expenses')

transactions = pd.DataFrame(df, columns=['Date','Type','Category','Amount','Details'])

transactions.to_csv(export_file, encoding='utf-8', index=False)
# print(transactions.head())