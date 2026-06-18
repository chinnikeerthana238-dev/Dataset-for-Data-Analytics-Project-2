import pandas as pd

df = pd.read_excel("Dataset for Data Analytics data.xlsx")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
numeric_df = df.select_dtypes(include=['number'])
print(numeric_df.corr())

import seaborn as sns
import matplotlib.pyplot as plt


plt.figure()
df["Country"].value_counts().head().plot(kind="pie", autopct="%1.1f%%")
plt.show()