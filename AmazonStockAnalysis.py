#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('Amzn_raw_data.csv', low_memory=False)
df.head() # Import & show top 5 rows


# In[4]:


import pandas as pd

file_path = 'amzn_raw_data.csv'  

df = pd.read_csv(file_path)

print(df.info())
print(df.head())


# In[5]:


df['date'] = pd.to_datetime(df['date'])


# In[6]:


df = pd.read_csv('Amzn_raw_data.csv', low_memory=False)
# Are there missing values?
print(df.isnull().sum())

# Fill missing values with median
# I do this with stock data, safest bet to preserve distribution
df['change_percent'].fillna(df['change_percent'].median(), inplace=True)
df['avg_vol_20d'].fillna(df['avg_vol_20d'].median(), inplace=True)


# In[7]:


df = df.drop_duplicates()


# In[8]:


# Convert 'volume' to int
# The volume numbers shouldn't be float numbers
df['volume'] = df['volume'].astype(int)


# In[9]:


# Descriptive statistics
print(df.describe())


# In[10]:


print(df.info())
print(df.head())


# In[13]:


# Financial Crisis period
financial_crisis_extended = df[(df['date'] >= '2007-01-01') & (df['date'] <= '2009-12-31')]

plt.figure(figsize=(12, 6))
plt.plot(financial_crisis_extended['date'], financial_crisis_extended['close'], color='red')
plt.title('Amazon Stock Price (2007-2009)')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.show()


# In[14]:


# COVID-19 period
covid_extended = df[(df['date'] >= '2019-01-01') & (df['date'] <= '2021-12-31')]

plt.figure(figsize=(12, 6))
plt.plot(covid_extended['date'], covid_extended['close'], color='green')
plt.title('Amazon Stock Price (2019-2021)')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.show()


# In[2]:


# Adding new Financial Data

import pandas as pd
import matplotlib.pyplot as plt

file_path_raw = 'amzn_raw_data.csv' 
file_path_adjusted = 'amzn_split_adjusted.csv' 

# Loading raw data
df_raw = pd.read_csv(file_path_raw)
df_raw['date'] = pd.to_datetime(df_raw['date'])

# Loading split-adjusted data
df_adjusted = pd.read_csv(file_path_adjusted)
df_adjusted['date'] = pd.to_datetime(df_adjusted['date'])

plt.figure(figsize=(12, 6))
plt.plot(df_raw['date'], df_raw['close'], label='Raw Closing Price', color='blue', alpha=0.7)
plt.plot(df_adjusted['date'], df_adjusted['close'], label='Split-Adjusted Closing Price', color='orange', alpha=0.7)

plt.title('Amazon Stock Price: Raw vs. Split-Adjusted')
plt.xlabel('Date')
plt.ylabel('Price (USD)')


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# Calculate percentage changes & plot

# Percentage change - closing price and volume
df_adjusted['price_change_pct'] = df_adjusted['close'].pct_change() * 100
df_adjusted['volume_change_pct'] = df_adjusted['volume'].pct_change() * 100

# Drop NaN values
df_adjusted.dropna(inplace=True)

# Correlation coefficient
correlation = df_adjusted['price_change_pct'].corr(df_adjusted['volume_change_pct'])

# Visualize relationship between change in volume and price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='volume_change_pct', y='price_change_pct', data=df_adjusted, alpha=0.5)
plt.title('Scatter Plot of % Change in Volume vs. % Change in Price')
plt.xlabel('% Change in Volume')
plt.ylabel('% Change in Price')
plt.axhline(0, color='gray', lw=1)
plt.axvline(0, color='gray', lw=1)
plt.grid(True)
plt.show()


# In[5]:


# 50-day SMA
df_adjusted['50_day_SMA'] = df_adjusted['close'].rolling(window=50).mean()

# Closing prices
plt.figure(figsize=(14, 7))
plt.plot(df_adjusted['date'], df_adjusted['close'], label='Actual Prices', color='blue', alpha=0.5)
plt.plot(df_adjusted['date'], df_adjusted['50_day_SMA'], label='50-Day SMA', color='orange', alpha=0.9)

plt.title('50-Day Moving Average and Actual Closing Prices')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price (USD)')
plt.legend()
plt.show()

most_recent_ma = df_adjusted['50_day_SMA'].iloc[-1]
print(f"The most recent 50-day SMA is: {most_recent_ma:.2f}")


# In[3]:


# Redo the Split adjusted code to add date
df_raw = pd.read_csv(file_path_raw)
df_raw['date'] = pd.to_datetime(df_raw['date'])

df_adjusted = pd.read_csv(file_path_adjusted)
df_adjusted['date'] = pd.to_datetime(df_adjusted['date'])

import pandas as pd
import matplotlib.pyplot as plt

stock_split_date = pd.Timestamp('2022-06-06')

plt.figure(figsize=(14, 7))
plt.plot(df_raw['date'], df_raw['close'], label='Raw Closing Price', color='blue', alpha=0.7)
plt.plot(df_adjusted['date'], df_adjusted['close'], label='Split-Adjusted Closing Price', color='orange', alpha=0.7)
plt.axvline(stock_split_date, color='green', linestyle='--', label='Stock Split on June 6, 2022')

plt.title('Amazon Stock Price: Raw vs. Split-Adjusted')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()


# In[ ]:




