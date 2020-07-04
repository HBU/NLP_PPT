# icwb2-data 数据集是由北京大学、香港城市大学、台湾 CKIP, Academia Sinica 及中国微软研究所联合发布的数据集，
# 用以进行中文分词模型的训练。
# 其中 AS 和 CityU 为繁体中文数据集，PK 和 MSR 为简体中文数据集。

from hmm import HMM

hmm_test = HMM()
hmm_test.train('icwb2-data/training/pku_training.utf8.txt')

text='我们在野生动物园玩'
res=hmm_test.cut(text)
print(text)
print(str(list(res)))

text='他是研究生物化学的'
res=hmm_test.cut(text)
print(text)
print(str(list(res)))

text='商品和服务'
res=hmm_test.cut(text)
print(text)
print(str(list(res)))

text='南京市长江大桥'
res=hmm_test.cut(text)
print(text)
print(str(list(res)))

text='下雨天留客天留我不留'
res=hmm_test.cut(text)
print(text)
print(str(list(res)))