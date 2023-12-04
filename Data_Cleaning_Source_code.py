import pandas as pd
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
import re
warnings.filterwarnings("ignore")
nltk.download('stopwords')
nltk.download('wordnet')

msg = pd.read_csv("./Message_Spam_Detection/dataset.csv",encoding='latin-1')
msg.drop(['Unnamed:2','unnamed:4'],axis=1,inplace=True)
msg.rename(columns={"v1":"label","v2":"text"},inplace=True)

for i in msg.index:
    if msg['label'][i] =='ham':
        msg['label'][i] = 0
    else:
        msg['label'][i] = 1
msg = msg.drop_duplicates()

msg['cleaned_text'] = ""
for i in msg.index:
    updated_list=[]
for j in range(len(msg['text'][i])):
    if msg['text'][i][j] notin string.punctuation:
        if msg['text'][i][j].isdigit() == False:
            updated_list.apppend(msg['text'][i][j])
msg['cleaned_text'][i] = updated_string
msg.drop(['text'],axis=1,inplace=True)

msg['token'] = ""
for i in msg.index:
    msg['token'][i] = re.split("\W+",msg['cleaned_text'][i].lower())
wordlem = nltk.WordNetLemmatizer()
for i in msg.index:
    updated_list = []
    for j in range(len(msg['updated_token'][i])):
        updated_list.append(wordlem.lemmatize(msg['ipdated_token'][i][j]))
    msg['lem_text'][i] = updated_list
msg.drop(['updated_token'],axis=1,inplace=True)
    
msg['final_text'] = ""
for i in msg.index:
    updated_string = "".join(msg['lem_text'][i])
    msg['final_text'][i] = updated_string
msg.drop(['cleaned_text','lem_text'],axis=1,inplace=True)
msg.to_csv('Cleaned_Dataset.csv')
