import pandas as pd
import re
import string
text=['This is introduction to NLP','It is likely to be useful,to people ',
'Machine learning is the new electrcity','Therewould be less hype around AI and more????? action goingforward',
'python is the best tool!','R is good langauage','Ilike this book',
'I want more books like this']
df = pd.DataFrame({'tweet':text})
print(df)
df['tweet'] = df['tweet'].apply(lambda line: " ".join(x.lower() for x in line.split()))
punc=string.punctuation
print(punc)
df['tweet']=df['tweet'].str.replace(punc,'')
print(df)



