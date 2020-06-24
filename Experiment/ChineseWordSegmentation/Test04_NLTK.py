import nltk
#nltk.set_proxy('http://proxy.example.com:3128', ('USERNAME', 'PASSWORD'))
#nltk.download()
#nltk.download('punkt')  又是一个大坑~ 这里怎么弄，都不能用。 慢慢总结吧。 学新东西是真不容易 2020.6.25 David
nltk.data.path.append("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\nltk_data")
#先分句再分词
sents = nltk.sent_tokenize("And now for something completely different. I love you.")
word = []
for sent in sents:
    word.append(nltk.word_tokenize(sent))
print(word)

#分词
text = nltk.word_tokenize("And now for something completely different.")
print(text)
#词性标注
tagged = nltk.pos_tag(text)
print (tagged[0:6])
#命名实体识别
entities = nltk.chunk.ne_chunk(tagged)
print (entities)