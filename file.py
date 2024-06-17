import time
import gensim.downloader as api
from gensim.models import Word2Vec
import pickle
import gensim
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from clean import get_max_count
def get_most_simmilar_dict(word,topn):
    vals = model.wv.most_similar(word,topn=topn)
    d = {k: i+2 for i,(k,v)in enumerate(vals)}
    return d
get_most_simmilar_dict('нога',10000)
data = []
for i in range(1,get_max_count()+1):
    with open(f'data/chunck_{i}.pickle','rb') as f:
        data += pickle.load(f)
data = [i for i in data if len(i)> 0]
print(f'Finded{len(data)}no blank sentences')
start_time = time.time()
model = Word2Vec(sentences=data,sg=1,vector_size=100,workers=8)
print(f'Time taken:{(time.time()- start_time)/60:.2f}mins')
model.wv.most_similar('нога')
model.wv.save_word2vec_format('custom_embedding.txt')
w2v = KeyedVectors.load_word2vec_format('custom_embedding.txt')
w2v.similarity('нога','рука')
model = api.load('word2vec=ruscorpora-300')
list(model.key_to_index.items())[:10]
d = {k.split('_')[0]: k for k in model.key_to_index}

model.similarity(d['нога'],d['рука'])
def get_most_similar_dict(word,topn):
    vals = model.most_similar(d[word],topn=topn)
    d_ = {k.split('_')[0]: i+2 for i,(k,v)in enumerate(vals)}
    return d_