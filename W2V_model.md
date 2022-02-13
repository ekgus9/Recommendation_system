# 한국어 미리 학습된 Word2Vec 모델 활용



- 박규병님의 모델 다운로드 : <https://drive.google.com/file/d/0B0ZXk88koS2KbDhXdWg1Q2RydlU/view>



- 사용법 : 

```
from gensim.models import Word2Vec, KeyedVectors

model = gensim.models.Word2Vec.load("ko.bin")
# 그대로 사용하면 에러가 발생하여 모델을 저장하여 사용
model.wv.save_word2vec_format("ko.bin.gz", binary=False)

# 해당 모델을 사용할 경우 vecter size는 200
model = Word2Vec(size=200, window=5, min_count=2, workers=4, sg=0)
model.build_vocab(corpus) # 학습시킬 코퍼스
model.intersect_word2vec_format("ko.bin.gz", binary=False) # 학습된 코퍼스 추가
model.train(corpus, total_examples = model.corpus_count, epochs = 15)
```

