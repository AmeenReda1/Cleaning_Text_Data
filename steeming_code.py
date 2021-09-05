text=['I like fishing','I eat fish','There are many fishes in pound']
#convert list to dataframe
import pandas as pd
df = pd.DataFrame({'tweet':text})
print(df)
#Import library
from nltk.stem import PorterStemmer
st = PorterStemmer()
df['tweet']=df['tweet'][:5].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
[print(df)]
