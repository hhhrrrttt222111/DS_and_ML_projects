import pandas as pd
import numpy as np
from textblob import TextBlob
import plotly.graph_objects as go
import plotly.express as px

trump = pd.read_csv("Trumpall2.csv")
biden = pd.read_csv("Bidenall2.csv")

# print(trump.head())
# print(biden.head())

textblob1 = TextBlob(trump["text"][10])
# print("Trump :", textblob1.sentiment)
textblob2 = TextBlob(biden["text"][500])
# print("Biden :", textblob2.sentiment)


def find_pol(review):
    return TextBlob(review).sentiment.polarity


trump["Sentiment Polarity"] = trump["text"].apply(find_pol)
# print(trump.tail())

biden["Sentiment Polarity"] = biden["text"].apply(find_pol)
# print(biden.tail())


trump["Expression Label"] = np.where(trump["Sentiment Polarity"]>0, "positive", "negative")
trump["Expression Label"][trump["Sentiment Polarity"]==0]="Neutral"
# print(trump.tail())

biden["Expression Label"] = np.where(biden["Sentiment Polarity"]>0, "positive", "negative")
biden["Expression Label"][trump["Sentiment Polarity"]==0]="Neutral"
# print(biden.tail())


reviews1 = trump[trump['Sentiment Polarity'] == 0.0000]
# print(reviews1.shape)

cond1=trump['Sentiment Polarity'].isin(reviews1['Sentiment Polarity'])
trump.drop(trump[cond1].index, inplace = True)
# print(trump.shape)

reviews2 = biden[biden['Sentiment Polarity'] == 0.0000]
# print(reviews2.shape)

cond2=biden['Sentiment Polarity'].isin(reviews1['Sentiment Polarity'])
biden.drop(biden[cond2].index, inplace = True)
# print(biden.shape)


# Donald Trump
np.random.seed(10)
remove_n =324
drop_indices = np.random.choice(trump.index, remove_n, replace=False)
df_subset_trump = trump.drop(drop_indices)
# print(df_subset_trump.shape)

# Joe Biden
np.random.seed(10)
remove_n =31
drop_indices = np.random.choice(biden.index, remove_n, replace=False)
df_subset_biden = biden.drop(drop_indices)
# print(df_subset_biden.shape)


count_1 = df_subset_trump.groupby('Expression Label').count()
# print(count_1)

negative_per1 = (count_1['Sentiment Polarity'][0]/1000)*10
positive_per1 = (count_1['Sentiment Polarity'][1]/1000)*100

count_2 = df_subset_biden.groupby('Expression Label').count()
# print(count_2)

negative_per2 = (count_2['Sentiment Polarity'][0]/1000)*100
positive_per2 = (count_2['Sentiment Polarity'][1]/1000)*100

Politicians = ['Joe Biden', 'Donald Trump']
lis_pos = [positive_per1, positive_per2]
lis_neg = [negative_per1, negative_per2]

fig = go.Figure(data=[
    go.Bar(name='Positive', x=Politicians, y=lis_pos),
    go.Bar(name='Negative', x=Politicians, y=lis_neg)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()
