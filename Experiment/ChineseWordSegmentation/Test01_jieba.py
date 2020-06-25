# https://baijiahao.baidu.com/s?id=1669982793268220871&wfr=spider&for=pc

# 精确模式 ： 在该模式下，Jieba会将句子进行最精确的切分
# 全模式 ： 把句子中所有可以成词的词语都扫描出来，优点在于该模式非常快，缺点也很明显，就是不能有效解决歧义的问题
# 搜索引擎模式 ：在精确模式的基础上，对长词进行再次切分，该模式适合用于搜索引擎构建索引的分词

import jieba
print("--------------------------------------------------------")
seg_list = jieba.cut("江大桥是计科二班的同学", cut_all=True)
print("全模式: " + "/ ".join(seg_list)) # 全模式
print("--------------------------------------------------------")
seg_list = jieba.cut("下雨天留客天留我不留", cut_all=False)
print("精确模式: " + "/ ".join(seg_list)) # 精确模式
print("--------------------------------------------------------")
seg_list = jieba.cut("江大桥是计科二班的同学") # 默认是精确模式
print(", ".join(seg_list))
print("--------------------------------------------------------")
str = "我是一个中国人"
word1 = jieba.cut_for_search(str) # 搜索引擎模式
for item in word1:
    print(item)