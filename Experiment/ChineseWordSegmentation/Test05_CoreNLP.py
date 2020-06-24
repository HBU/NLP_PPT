# 安装：pip install stanfordcorenlp
# 先下载模型，下载地址：https://nlp.stanford.edu/software/corenlp-backup-download.html
# 支持多种语言，这里记录一下中英文使用方法
from stanfordcorenlp import StanfordCoreNLP

zh_model = StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='zh')
en_model = StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='en')
zh_sentence = '我爱自然语言处理技术！'
en_sentence = 'I love natural language processing technology!'
print ('Tokenize:', zh_model.word_tokenize(zh_sentence))
print ('Tokenize:', en_model.word_tokenize(en_sentence))

# https://cloud.tencent.com/developer/article/1437813