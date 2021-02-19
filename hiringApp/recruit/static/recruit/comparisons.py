from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import gensim
import numpy as np

file_doc = []
with open('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/static/recruit/'
          'Python_junior_developer_requirements.txt') as f:
    s = sent_tokenize(f.read())
    for sentence in s:
        file_doc.append(sentence)

gen_docs = [[w.lower() for w in word_tokenize(text)] for text in file_doc]
dictionary = gensim.corpora.Dictionary(gen_docs)
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
tf_idf = gensim.models.TfidfModel(corpus)

sims = gensim.similarities.Similarity('newdir', tf_idf[corpus], num_features=len(dictionary))

file2_doc = []
with open('C:/Users/Lenovo-User/PycharmProjects/newApp/hiringApp/recruit/static/recruit/Sample CV text.txt') as f:
    s = sent_tokenize(f.read())
    for sentence in s:
        file2_doc.append(sentence)

for line in file2_doc:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc)

query_doc_tf_idf = tf_idf[query_doc_bow]
sum_of_sims = (np.sum(sims[query_doc_tf_idf], dtype=np.float32))
percentage_of_similarity = round(float((sum_of_sims/len(file_doc)) * 100))
print('Percentage of similarity: ', percentage_of_similarity, '%', sep="")
