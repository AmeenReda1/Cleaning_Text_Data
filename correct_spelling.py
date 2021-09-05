from textblob import TextBlob
#convert list to dataframe
import pandas as pd
from autocorrect import spell
text=['Introduction to NLP','It is likely to be useful, to people ',
'Machine learning is the new electrcity', 'R is good langauage',
'I like this book','I want more books like this']
df = pd.DataFrame({'tweet':text})
print(df)
df['tweet']=df['tweet'].apply(lambda x: str(TextBlob(x).correct()))
print(df)
print(spell(u'mussage'))
print(spell(u'sirvice'))
