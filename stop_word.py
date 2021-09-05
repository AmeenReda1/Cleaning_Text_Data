import pandas as pd
import nltk
nltk.download()
from nltk.corpus import stopwords
text=['this is introduction to NLP','It is likely to be useful,to people ',
'Machine learning is the new electrcity',
'There would be less hype around AI and more action goingforward',
'python is the best tool!','R is good langauage','I likethis book',
'I want more books like this']
df = pd.DataFrame({'tweet':text})
#print(df)
stop = stopwords.words('english')
print(stop)
df['tweet'] = df['tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
print(df['tweet'])
# stop word is commen word and useless word in english for example "how to use chatbot python" << how and to is stop word