# Bitcoin Price Prediction model - LSTM | Multivariable (Price&Polarity) Time Series Forecasting with NLP for Twitter Sentiments

Two Long Short Term Memory based models with 4 layers (2xLSTM & 2xDense) for BTC price prediction.
Model I (3_model_I_LSTM_CoinMarketCap.ipynb) has only 1 variable - BTC Close Price and therefore is predicting the prices using 60 days time series of price values for predicting the actual prices.
Model II (4_model_II_imp.ipynb) - multivariable (two variables - price and polarity) time series prediction - time series is again 60 days and model is learning from both price and sentiment values for those 60 days.

Feature engineering:
 - to calculate polarity TextBlob library was used - through that Twitter sentiment score could be calculated both by polarity and subjectivity score, but as our data comes from social media, subjectivity score would give obvious input
 - from BTC prices Close Price value was used
 - correlation between those two variables was calculated and is equal to 0.77

Data:
- 2 x Kaggle datasets (6,24 GB / 25M Tweets) as Twitter API doesn't allow to get historical data
- Yahoo Finance BTC Price table starting from 2014

Additional information:
This is my Masters Thesis (University of Warsaw, Big Data Management '23).

For data preparation for the 2nd model, I have used Jason Brownlee's function series_to_supervised() from "How to Convert a Time Series to a Supervised Learning Problem in Python" (2017) and some of the data scaling, transforming and inverse transforming tricks mentioned in Ruslan Magana Vsevolodovna's article "Multivariable Time Series Forecasting with Neural Networks" (2020).
