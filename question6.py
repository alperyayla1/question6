import pandas as pd
import numpy as np
import statistics
df = pd.read_csv("C:/Users/alper/Downloads/country_vaccination_stats (1).csv")
country_grouped_df = df.groupby("country")

top_three_median = np.array([0,0,0])
top_three_country = np.empty([3,1],dtype=('U100'))
for country, group in country_grouped_df:

    if pd.isna(group['daily_vaccinations']).all():

        group['daily_vaccinations'].fillna(0, inplace=True)
        df.loc[group.index, 'daily_vaccinations'] = group['daily_vaccinations']
    else:


        min_value = group['daily_vaccinations'].min()

        group['daily_vaccinations'].fillna(min_value, inplace=True)
        df.loc[group.index, 'daily_vaccinations'] = group['daily_vaccinations']

    median = statistics.median(group['daily_vaccinations'])
    if(median > np.min(top_three_median)):

        min_index = np.argmin(top_three_median)
        top_three_median[min_index] = median
        top_three_country[min_index] = group["country"].iloc[0]
print("The top-3 countries with highest median:")
for i in range(0,3):
    print("{} : {}".format(top_three_country[i],top_three_median[i]))


df.to_csv('updated_data1.csv', index=False)

