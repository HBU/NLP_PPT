# 斯坦福 Stanford 
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'/home/gld/stanford-corenlp-full-2016-10-31/', lang='zh')
sentence = '清华大学位于北京。'
print nlp.word_tokenize(sentence)
print nlp.pos_tag(sentence)
print nlp.ner(sentence)
print nlp.parse(sentence)
print nlp.dependency_parse(sentence)