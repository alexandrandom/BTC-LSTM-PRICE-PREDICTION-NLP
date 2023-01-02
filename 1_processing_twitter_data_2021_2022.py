import pandas as pd
print("imported")
#2GB, so decided to import only 2 columns in pandas bc when I was processing it through Dask, exporting the files to csv was giving EOF errors that couldn't be fixed by specifying encoding, separator, engine='python', or other csv parameters, nor couldn't they be omitted. 
rlybigdata=pd.read_csv(r"C:\Users\ACJ\Downloads\Bitcoin_tweets.csv", engine='python', usecols=['date', 'text'])

rlybigdata.to_csv(r"C:\Users\ACJ\Downloads\ANwork.csv",index=False)
print("saved")


df=pd.read_csv(r'C:\Users\ACJ\Downloads\ANwork.csv')


from textblob import TextBlob as tb
#defining the function that will calculate the polarity score of a given text item - tweet
def calculate_polarity(tweet):
    analysis = tb(tweet)
    out=analysis.sentiment.polarity
    
    return out

#defining new list for sentiments
sweet_emotion=[] #hehe got the reference?

#iterating over the tweet column
for item in df["text"]:
  str_fr=str(item) #needed to add that bc previous code crashed at 4383361st item
  sweet_emotion.append(calculate_polarity(str_fr))


print(len(sweet_emotion))
df["sentiment"]=sweet_emotion

df2=df.drop(["text"], axis=1)
df2[['date', 'time']] = df2['date'].str.split(' ', 1, expand=True)

#reading the csv with stock prices
prices=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DATA_1/BTC-USD.csv", engine='python')
prices = prices[['Date', 'Close']]

#left joining two dataframes together by date so that we have the prices and sentiments for each day that we have tweets for
df_merged=df2.merge(prices, left_on='date', right_on="Date", how='left')

#creating a new DF
dates=[]
sentiments=[]
prices=[]

for i in df_merged["date"]:
  dates.append(str(i))
for i in df_merged["sentiment"]:
  sentiments.append(float(i))
for i in df_merged["Close"]:
  prices.append(float(i))

test_one=pd.DataFrame()
test_one["dates"]=dates
test_one["prices"]=prices
test_one["sentiment"]=sentiments

#exporting the new file
toexport=test_one.groupby(["dates", "prices"]).agg({"sentiment":"mean"})
toexport.to_csv("/content/drive/MyDrive/Colab Notebooks/DATA_1/TESTOWE.csv")
