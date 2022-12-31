import pandas as pd
print("imported")
#2GB, so decided to import only 2 columns in pandas bc when I was processing it through Dask, exporting the files to csv was giving EOF errors that couldn't be fixed by specifying encoding, separator, engine='python', or other csv parameters, nor couldn't they be omitted. 
rlybigdata=pd.read_csv(r"C:\Users\ACJ\Downloads\Bitcoin_tweets.csv", engine='python', usecols=['date', 'text'])

rlybigdata.to_csv(r"C:\Users\ACJ\Downloads\ANwork.csv",index=False)
print("saved")

df=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/DATA_1/ANwork.csv", engine='python')

#plot twist - importing libraries in the middle of code
#this is a NLP lib
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
