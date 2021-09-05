text=['I like fishing','I eat fish','There are many fishes in pound','best work','leaves and leaf']
#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)
#Import library
from textblob import Word
df['tweet']=df['tweet'].apply(lambda line: " ".join([Word(word).lemmatize() for word in line.split()]))
print(df)