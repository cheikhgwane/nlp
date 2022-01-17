from sklearn.preprocessing import OneHotEncoder
import pandas as pd

sampleSentence = "The cat sat on the mat"

data = [[x] for x in sampleSentence.split()]
df = pd.DataFrame.from_dict({"Word" :sampleSentence.split()})

encoder = OneHotEncoder(handle_unknown="ignore")
encodedDf =  pd.DataFrame(encoder.fit_transform(data).toarray())

df = df.join(encodedDf)
print(df)