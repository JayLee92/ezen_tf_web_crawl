from konlpy.tag import Okt
import re

#import nltk
#nltk.download()
from nltk.tokenize import word_tokenize

ctx = r'C:\Users\ezen\PycharmProjects\test2\data\\'
filename = ctx + 'kr-Report_2018.txt'
#r은 read only
with open(filename,'r',encoding='UTF-8') as f:
    texts = f.read()
#print(texts[:300])

texts = texts.replace('\n','')
tokenizer = re.compile('[^ ㄱ-힣]+')
texts = tokenizer.sub('',texts)

tokens = word_tokenize(texts)

print(texts[:7])