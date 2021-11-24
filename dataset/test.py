import csv
import re
import pandas as pd

# with open(r'D:\FakeHealth-master\dataset\replies_infos-sujo.csv','r',encoding="UTF-8") as f:
#     file = csv.reader(f)
#     data = list(file)
#     print(data)
# sep = "..."
# #print(data[5][1])
# data = data[1:]
# for item in data:
#     text, sep, tail = item[1].partition('https')
#     if sep !="":
#         no_https = text[:-2]
#     else: no_https = text
#     pos = no_https.find("@")
#     first_space = no_https.find(" ")
#     last_space = no_https.rfind(" ")
#     if no_https.find("@") != -1:
#         reply = no_https[first_space+1:]
#     else: reply = no_https
#     item[1] = reply
# 
# 
# df = pd.DataFrame(data,columns = ["reply_id","text","news_source"])
# print(df)
# df.to_csv('replies_infos_novo.csv',encoding='utf-8',index=False)

# #Cleaning dataset and creating txt to PRADO
# 
# with open(r'D:\FakeHealth-master\dataset\replies_infos.csv','r',encoding="UTF-8") as f:
#     file = csv.reader(f)
#     data = list(file)
# replies_text =[]
# 
# for item in data:
#     no_skip = item[1].replace("\n", " ")
#     only_english = re.sub("[^a-zA-Z0-9]+"," ",no_skip)
#     if(only_english != " "):
#         replies_text.append(only_english)
#     item[1] = only_english
# 
# df = pd.DataFrame(data)
# df.to_csv("clean_replies.csv")
# 
# 
# 
# #print(replies_text[5])
# with open('replies_text1.txt','w',encoding="utf-8") as f:
#     for item in replies_text[:1000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text2.txt','w',encoding="utf-8") as f:
#     for item in replies_text[1001:2000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text3.txt','w',encoding="utf-8") as f:
#     for item in replies_text[2001:3000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text4.txt','w',encoding="utf-8") as f:
#     for item in replies_text[3001:4000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text5.txt','w',encoding="utf-8") as f:
#     for item in replies_text[4001:5000]:
#         f.write("b'%s',\n"%item) 
# with open('replies_text6.txt','w',encoding="utf-8") as f:
#     for item in replies_text[5001:6000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text7.txt','w',encoding="utf-8") as f:
#     for item in replies_text[6001:7000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text8.txt','w',encoding="utf-8") as f:
#     for item in replies_text[7001:8000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text9.txt','w',encoding="utf-8") as f:
#     for item in replies_text[8001:9000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text10.txt','w',encoding="utf-8") as f:
#     for item in replies_text[9001:10000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text11.txt','w',encoding="utf-8") as f:
#     for item in replies_text[10001:11000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text12.txt','w',encoding="utf-8") as f:
#     for item in replies_text[11001:12000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text13.txt','w',encoding="utf-8") as f:
#     for item in replies_text[12001:13000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text14.txt','w',encoding="utf-8") as f:
#     for item in replies_text[13001:14000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text15.txt','w',encoding="utf-8") as f:
#     for item in replies_text[14001:15000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text16.txt','w',encoding="utf-8") as f:
#     for item in replies_text[15001:16000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text17.txt','w',encoding="utf-8") as f:
#     for item in replies_text[16001:17000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text18.txt','w',encoding="utf-8") as f:
#     for item in replies_text[17001:18000]:
#         f.write("b'%s',\n"%item)
# with open('replies_text19.txt','w',encoding="utf-8") as f:
#     for item in replies_text[18001:]:
#         f.write("b'%s',\n"%item)
#         
#         
#         
#         
#         
# df =pd.DataFrame(replies_text)
# df.to_csv('test_out.csv',encoding="utf-8",index = False)

#Parsing PRADO output

texts_final =[]
only_emotions_final =[]
parsed_dirty_output = []
j = 1
while j < 20:
   f = open(r'D:\FakeHealth-master\dataset\replies_text{} OUTPUT.txt'.format((j)), 'r')
   lines = f.read().split('\n')
   texts = []
   first_emotion = []
   only_emotion = []
   parsed_dirty_output = []
   entry = []
   no_empties = []

   #tira linhas vazias
   for i in range(len(lines)):
       if lines[i] != '':
           no_empties.append(lines[i])
           
   #pega os textos
   i = 0
   while i in range(len(no_empties)):
       texts.append(no_empties[i])
       i = i + 4
   
   #pega a primeira emoção
   i = 1
   while i in range(len(no_empties)):
       first_emotion.append(no_empties[i])
       i = i + 4
   
   #pega so o nome da primeira emoção
   i = 0
   while i in range(len(first_emotion)):
       emotion_name = first_emotion[i].split(':')[0]
       only_emotion.append(emotion_name)
       i = i + 1

       
   texts_final = texts_final + texts
   only_emotions_final =only_emotions_final + only_emotion
       
   j = j+1
   
i=0
while i in range(len(texts_final)):
     entry = [texts_final[i],only_emotions_final[i]]
     parsed_dirty_output.append(entry)
     i = i+1


df =pd.DataFrame(parsed_dirty_output)
df.to_csv('prado_parsed_dirty_output.csv',encoding="utf-8",index = False)

    