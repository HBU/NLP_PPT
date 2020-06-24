# https://github.com/Windsooon/cherry

import cherry
res = cherry.classify(model='news', text=['她们对计算机很有热情，也希望学习到数据分析，网络爬虫，人工智能等方面的知识，从而运用在她们工作上'])

print(res.word_list)

print('------返回结果分别对应 彩票 / 科技 / 财经 / 房产 / 社会 / 体育 / 娱乐 类别的概率---------')
print(res.probability)