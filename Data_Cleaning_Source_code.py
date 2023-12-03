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
