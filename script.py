import pandas as pd
import numpy as np

df = pd.read_csv("./marketing.csv", delimiter=",")

print(df.head(5))

print(df.describe(include="all"))

print(df.info())

print(df['converted'].head(5))

print(df['converted'].dtype)

(df['converted']) = print(df['converted'].astype('bool'))

print(df)

np.where(df['marketing_channel'] == 'House Ads', True, False)

channel_dict = {
    'House Ads': 1,
    'Instagran' : 2,
    'Facebook': 3,
    'Email': 4,
    'Push': 5,
    '': 0
}

print(df['marketing_channel'].map(channel_dict))




