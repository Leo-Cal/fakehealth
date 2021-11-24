import json, os
import pandas as pd
import numpy as np
import mysql.connector
import sqlalchemy
import pickle


def get_replies():
    id= []
    text =[]
    reply_entry =[]
    news_infos = []
    directory_str = r"D:\FakeHealth-master\dataset\engagements\HealthRelease"
    for root, dirs, files in os.walk(os.path.join(directory_str), topdown=False):
        for name in files:
            #print("rodando files %s", )
            if "replies" in os.path.join(root,name):
                print("Reading at %s",os.path.join(root, name))
                #Contar retweets:
                path0 = os.path.join(root)[:-8]
                path1= "retweets"
                path2 = r'{}\{}'.format(path0, path1)
                #print(path2)
                num_retweets = len(os.listdir(path2))
                
                #Construir o ID da noticia referencia:
                ref1 = os.path.join(root)[-13:-8]
                ref2 = "NR"
                reference= ref2+ref1
                
                with open(os.path.join(root, name)) as filename:
                    data = json.load(filename)
                    reply_entry.append([data["id_str"],data["text"],reference])
                    #id.append(data["id_str"])
                    #text.append(data["text"])
        for name in dirs:
            if "replies" in os.path.join(root,name):
                name = os.path.join(root, name, r"\replies")
                #print(os.path.join(root, name))
            #stuff
    
    directory_str = r"D:\FakeHealth-master\dataset\engagements\HealthStory"
    for root, dirs, files in os.walk(os.path.join(directory_str), topdown=False):
        for name in files:
            #print("rodando files %s", )
            if "replies" in os.path.join(root,name):
                print("Reading at %s",os.path.join(root, name))
                # Contar retweets:
                path0 = os.path.join(root)[:-8]
                path1 = "retweets"
                path2 = r'{}\{}'.format(path0, path1)
                # print(len(os.listdir(path2)))
                
                #Pegar ID da noticia referencia
                ref1 = os.path.join(root)[-13:-8]
                ref2 = "SR"
                reference = ref2 + ref1
                with open(os.path.join(root, name)) as filename:
                    data = json.load(filename)
                    reply_entry.append([data["id_str"],data["text"],reference])
                    #id.append(data["id_str"])
                    #text.append(data["text"])
                    #print(id)
        for name in dirs:
            if "replies" in os.path.join(root,name):
                name = os.path.join(root, name, r"\replies")
                #print(os.path.join(root, name))
            #stuff
    
    df = pd.DataFrame(reply_entry)
    df.to_csv('replies.csv',index=False)
    
    #with open('texts.txt', 'wb') as text_output:
    #    pickle.dump(text,text_output)
    #with open('ids.txt', 'wb') as ids_output:
    #    pickle.dump(id,ids_output)
    #with open('text_string.txt', 'w', encoding='utf-8') as f:
    #    for item in text:
    #        f.write("%s\n" % item)
    #with open ('ids_string.txt', 'w', encoding='utf-8') as f:
    #    for item in id:
    #        f.write("%s\n" % item)
    
    #df = pd.DataFrame(list(zip(id,text)), columns= ['id','text'])
    #print(df)
    
    #database_connection = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/fakenewsnet')
    #df.to_sql(con=database_connection,name="replies", index=False, if_exists='replace')
    #mysql+pymysql://root:root@localhost:3306/fakenewsnet
    #with open("ids.txt") as id_file:
     #  for item in id:
      #      id_file.write("{}\n".format(item))
    #with open("texts.txt") as text_file:
     #   for item in text:
      #      text_file.write("{}\n".format(item))
    
    #print(id)
    #print(text)
    #mydb = mysql.connector.connect(
    #  host="localhost",
    #  user="root",
    #  password="root",
    #  database="fakenewsnet"
    #)
    
    #mycursor = mydb.cursor()
    
    #sql = "INSERT INTO laptop
    

def get_news_infos():
    news_infos = []
    folder = r"D:\FakeHealth-master\dataset\engagements\HealthRelease"
    
    for i in range (606):
        folder_number = "{:05d}".format(i)
        final_path = r'{}\{}_{}\{}'.format(folder,"news_reviews",folder_number,"retweets")
        num_retweets = len(os.listdir(final_path))
        final_path = r'{}\{}_{}\{}'.format(folder, "news_reviews", folder_number, "replies")
        num_replies = len(os.listdir(final_path))
        final_path = r'{}\{}_{}\{}'.format(folder, "news_reviews", folder_number, "tweets")
        num_tweets = len(os.listdir(final_path))
        id = r'{}{}'.format("NR",folder_number)
        news_infos.append([id,num_replies,num_retweets,num_tweets])

    folder = r"D:\FakeHealth-master\dataset\engagements\HealthStory"
    for i in range (1700):
        if(i != 1080 and i != 1200 and i != 1201 and i != 1305 and i != 1335 and i != 1457 and i != 1458 and i != 1470 and i != 1545 and i != 1696) :
            folder_number = "{:05d}".format(i)
            final_path = r'{}\{}_{}\{}'.format(folder,"story_reviews",folder_number,"retweets")
            num_retweets = len(os.listdir(final_path))
            final_path = r'{}\{}_{}\{}'.format(folder, "story_reviews", folder_number, "replies")
            num_replies = len(os.listdir(final_path))
            final_path = r'{}\{}_{}\{}'.format(folder, "story_reviews", folder_number, "tweets")
            num_tweets = len(os.listdir(final_path))
            id = r'{}{}'.format("SR",folder_number)
            news_infos.append([id,num_replies,num_retweets,num_tweets])
    
    df = pd.DataFrame(news_infos,columns=["id","num_replies","num_retweets","num_tweets"])
    df.to_csv('news_infos.csv', index=False)

        #folder_name = r'{}\{}'.format(path0, path1)
        #print('Searching in:', base)
        #for directories in dirs:
            #if("retweets" in directories):
            #     ref1 = os.path.join(base)[-5:]
            #     ref2 = "NR"
            #     reference = ref2 + ref1
            #     print(reference)
            #     #news_infos.append([reference,num_retweets])
            #     #print(news_infos)
                
            
    
    

def main():
    print("entering function")
    get_news_infos()
    return 0

if __name__ == "__main__":
    main()