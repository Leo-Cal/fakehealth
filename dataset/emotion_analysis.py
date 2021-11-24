from nrclex import NRCLex
import pickle
import pandas as pd
import numpy as np
import mysql.connector
import sqlalchemy


columns = ['text','fear','anger','anticipation','trust','surprise','positive','negative','sadness','disgust','joy']
texts_list=[]
fear=[]
anger=[]
anticipation=[]
trust=[]
surprise=[]
positive=[]
negative=[]
sadness=[]
disgust=[]
joy=[]
with open('texts.txt', 'rb') as f:
    text = pickle.load(f)

for i in range (len(text)):
    emotion = NRCLex(text[i])
    dict = emotion.affect_frequencies
    texts_list.append(text[i])
    fear.append(dict["fear"])
    anger.append(dict["anger"])
    anticipation.append(dict["anticip"])
    trust.append(dict["trust"])
    surprise.append(dict["surprise"])
    positive.append(dict["positive"])
    negative.append(dict["negative"])
    sadness.append(dict["sadness"])
    disgust.append(dict["disgust"])
    joy.append(dict["joy"])
    #print('\n\n', text[i], ': ', emotion.affect_frequencies)

df = pd.DataFrame(list(zip(texts_list,fear,anger,anticipation,trust,surprise,positive,negative,sadness,disgust,joy)), columns= columns)
df.to_csv(r'D:\FakeHealth-master\dataset\nrclex_output.csv', sep='\t',index=False)
print(df)

#df = pd.DataFrame.from_dict(dict, orient='index')
#df.reset_index(level=0, inplace=True)
#print(df)

#database_connection = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/fakenewsnet')
#df.to_sql