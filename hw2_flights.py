import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import sqlite3

con = sqlite3.connect('mydb.sqlite')

sql = "SELECT name FROM sqlite_master WHERE type='table'"

pd.read_sql(sql, con)

df = pd.read_sql("SELECT * FROM flights", con)

# Question 1

# Removing the distant outliers -- Hawaii and Alaska
df = df[df['distance'] < 3000]

f = sns.jointplot(data=df, x="distance", y="arr_delay")
f.savefig('figs/Joint histogram of distance vs delay')

# Question 2

df = df.groupby('dest').mean()

f = df.plot.scatter("distance", "arr_delay")
f.get_figure().savefig('figs/Distance vs arrival delay grouped by dest')

# Question 3

from itertools import chain, combinations

df = pd.read_csv('flights.csv');

fields = ['year', 'month', 'day', 'hour', 'flight']

def key_options(items):
    return chain.from_iterable(combinations(items, r) for r in range(len(items), len(items)+1))

# iterate over the given fields
for candidate in key_options(fields):
    deduped = df.drop_duplicates(candidate)
    
    print('Column:', candidate)
    print('Indexable rows:', len(deduped.index))
    print('Total rows:', len(df.index))
    if len(deduped.index) == len(df.index):
        print('Yes, the grayed columns can be primary key')
    else:
        print('No, the grayed columns cannot be primary key')
        
# Question 4

df1 = pd.read_sql("SELECT carrier, tailnum, month, day FROM flights WHERE tailnum IN (SELECT tailnum FROM planes WHERE manufacturer = 'AIRBUS INDUSTRIE') LIMIT 10", con)
print(df1)

df2 = pd.read_sql("SELECT flights.carrier, flights.tailnum, flights.month, flights.day FROM flights INNER JOIN planes ON flights.tailnum=planes.tailnum WHERE planes.manufacturer = 'AIRBUS INDUSTRIE' LIMIT 10", con)
print(df2)

if df1.equals(df2):
    print("Yes, both queries produce same results")
else:
    print("No, both queries produce different results")
