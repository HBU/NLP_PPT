import nltk

#解析中文
#做中文分词解析，分割符一定要用“.”才可以正确识别解析（“.”后面一定要一个空格）

text1 = '同是风华正茂，怎敢甘拜下风 . 保持学习，保持饥饿'
Juzi_chinese = nltk.sent_tokenize(text1)
print(Juzi_chinese)