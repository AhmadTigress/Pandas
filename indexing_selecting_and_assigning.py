# -*- coding: utf-8 -*-
"""Indexing_Selecting_and_Assigning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1esQvOkChLipbmP3dE9weFi1hnoBOk2sE
"""

import pandas as pd
reviews = pd.read_csv("/content/winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)

"""**Native accessors**"""

reviews

reviews.country

reviews['country']

reviews['country'][0]

"""**Indexing in pandas**

*Index-based selection*
"""

reviews.iloc[0]

reviews.iloc[:, 0]

reviews.iloc[:3, 0]

reviews.iloc[1:3, 0]

reviews.iloc[[0, 1, 2], 0]

reviews.iloc[-5:]

"""*Label-based selection*"""

reviews.loc[0, 'country']

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

"""**Manipulating the index**"""

reviews.set_index("title")

"""**Conditional selection**"""

reviews.country == 'Italy'

reviews.loc[reviews.country == 'Italy']

reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]

reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)]

reviews.loc[reviews.country.isin(['Italy', 'France'])]

reviews.loc[reviews.price.notnull()]

"""**Assigning data**"""

reviews['critic'] = 'everyone'
reviews['critic']

reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']

