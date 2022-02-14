import pandas as pd
import numpy as np
import re
from gensim.models import Word2Vec, KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt

okt = Okt()

text = pd.read_excel('netflix_sep.xlsx')
text = pd.DataFrame(text)

text_delete = []
for i in range(len(text)):
    a = re.compile('[,.?/\'\"\[\]\{\}\|\+\=\-_\)\(\*\&\^!~$%#\�\《\》]')
    a = a.sub('',text.iloc[i][5])
    a = okt.morphs(a)
    text_delete.append(a)
    
# 불용어 제거
stopwords = ['은','는','으로','의','을','를','가','이','하','것','들','그','되','수','보','않','없','니','아니','등','때','지','오','그것','두','그러나','더','그리고','중','속','적','데','경우','이런','번','개','싶','좀']
text_stop = []
for i in text_delete:
    text_stop.append(' '.join([j for j in i if j not in stopwords]))

corpus = []
for w in text_stop:
    corpus.append(w.split())

ko = Word2Vec.load("C:/Users/user/Downloads/ko/ko.bin")
ko.wv.save_word2vec_format("ko.bin.gz", binary=False)
model = Word2Vec(size=200, window=5, min_count=2, workers=4, sg=0)
model.build_vocab(corpus)
model.intersect_word2vec_format("ko.bin.gz", binary=False)
model.train(corpus, total_examples = model.corpus_count, epochs = 15)
model.wv.save_word2vec_format("recommend.bin.gz", binary=False)
embedding = []

for i in corpus:
    vec = None
    count = 0
    for j in i: 
        if j in model.wv.vocab: 
            count += 1
            if vec is None:
                vec = model.wv[j]
            else:
                vec = vec + model.wv[j]
        
    if vec is not None:
        vec = vec / count
        embedding.append(vec)
        
cosine_similarities = cosine_similarity(embedding, embedding)

def recommendations(title):

    if title in text.iloc[:,0].to_list():
        idx = text.index[text['제목']==title]

    # 유사한 5개 선정
    sim_scores = list(enumerate(cosine_similarities[idx[0]])) # idx의 타입은 int64index
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:6]

    # 가장 유사한 5 인덱스
    book_indices = [i[0] for i in sim_scores]
    
    return book_indices

result = recommendations('진격의 거인')
sim_list = []

for i in range(len(result)):
    sim_list.append(text.iloc[result[i]])
    
#sim_list[0][0]