import pandas
import matplotlib.pyplot as plt

#this defines the series, so it will look in Pandas and find the series code
series = pandas.Series([10, 15, 21])
# the date is written in U.S form:
dates = pandas.date_range('20180920', '20180930')

df = pandas.DataFrame([[10, 15],[21, 17],[1, 5]],
                    columns=['money', 'happiness'],
                    index=['Bob', 'Tom', 'Olivia'])

#these can be typed in the bottom right box so you can see the print
print(df.dtypes)
print(df.columns)
print(df.index)
df.describe()

# to find out the money values in the data frame:
df['money']
# to find the information in row 0 column 2:
df[0:2]
# to get information for one of the string values in the data frame type:
df.loc['Bob', 'money']
# to locate the interger, type: 
df.iloc[1,0]


# here, we input the Leeds pub information from a csv file
pubs = pandas.read_csv('https://files.datapress.com/leeds/dataset/leeds-beer-quest/2017-06-19T09:00:57.81/leedsbeerquest.csv')
print(pubs)
# to find the mean we can type:
pubs.lat.mean()
#to find out information for one of the pubs called Veritas, we have to use the
# 'loc.' as this can only search for words and not numbers. 
named_pubs = pubs.set_index('name')
named_pubs.loc['Veritas']
# we're now going to find the cheap pubs
pubs.stars_value
pubs.stars_value.value_counts()
# 5 star value pubs:
named_pubs.stars_value == 5
# find the name of the pubs 
named_pubs[named_pubs.stars_value == 5].index
# want to find the address
named_pubs[named_pubs.stars_value == 5].address
#to get a histogram
named_pubs.stars_value.hist(bins=9)

named_pubs.groupby('stars_value').mean()

#lat of pubs
named_pubs.lat
#long of pubs
named_pubs.lng
# plot a graph of lat and long of pubs
plt.plot(pubs.lat, pubs.lng)
# plot a more geographical plot with a colour bar
plt.hexbin(pubs.lat, pubs.lng, gridsize = 15); plt.colorbar()