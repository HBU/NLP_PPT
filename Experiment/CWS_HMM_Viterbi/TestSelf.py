#####测试
from hmm import HMM

hmm_test = HMM()
hmm_test.train('CWS_HMM/trainCorpus.txt_utf8.txt')

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