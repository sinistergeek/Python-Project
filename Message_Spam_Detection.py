import pandas as pd
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidTransformer
from sklearn.ensemble import RandomForestClassifier
import pickle
import warnings
import re
warnings.filterwarnings("ignore")

msg = pd.read_csv("./Message_Spam_Detection/Cleaned_Dataset.csv",encoding='latin-1')

msg.drop(['Unnamed: 0'],axis=1,inplace=True)
y = pd.DataFrame(msg.label)
x = msg.drop(['label'],axis=1)
cv = CountVectorizer(max_features=50000)
temp1 = cv.fit_transform(x['final_text'].values.astype('U')).toarray()
tf = TfidfTransformer()
temp1 = tf.fit_transform(temp1)
temp1 = pd.DataFrame(temp1.toarray(),index=x.index)
x=pd.concat([x,temp1],axis=1,sort=False)

x.drop(['final_text'],axis=1,inplace=True)
y=y.astype(int)
model = RandomForestClassifier(n_estimators=100,random_state=0)
model.fit(x,y)

text = input("Enter text: ")

updated_text = ''
for i in range(len(text)):
    if text[i].isdigit() == False:
        updated_text = updated_text + text[i]
text = updated_text

text = re.split("\W+",text.lower())

updated_list = []
stopwords = nltk.corpus.stopwords.words('english')
for i in range(len(text)):
    if text[i] not in stopwords:
        updated_list.append(text[i])
text = updated_list

text = "".join(text)
text = cv.transform([text])
pred = model.predict(text)
if pred == 0:
    print("Not Spam")
else:
    print("Spam")
