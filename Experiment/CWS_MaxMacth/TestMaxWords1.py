# https://zhuanlan.zhihu.com/p/103392455
# 正向最大匹配法（FMM，Forward Maximum Matching）
# 反向最大匹配法（BMM, Backward Maximum Matching）
# 双向最大匹配法 首先看两种方法结果的分词数，分词数越少越好；分词数相同的情况下，看单个词的数量，越少越好

from FMM import FMM_func
from BMM import BMM_func

sentence = '我们在野生动物园玩'
user_dict = ['我们', '在', '在野', '生动', '野生', '动物园', '野生动物园', '园','玩']

FMM_func(user_dict, sentence)
print()
BMM_func(user_dict, sentence)

# 如：“我们在野生动物园玩”
# 正向最大匹配法，最终切分结果为：“我们/在野/生动/物/园/玩”，其中，两字词3个，单字字典词为2，非词典词为1（'物'不在词典）。
# 逆向最大匹配法，最终切分结果为：“我们/在/野生动物园/玩”，其中，五字词1个，两字词1个，单字字典词为2，非词典词为0。
# 非字典词：正向(1)>逆向(0)（越少越好）
# 单字字典词：正向(2)=逆向(2)（越少越好）
# 总词数：正向(6)>逆向(4)（越少越好）
# 因此最终输出为：逆向结果。逆向结果是正确的。
