# https://www.cnblogs.com/dahuang123/p/11990651.html


from FMM import FMM_func
from BMM import BMM_func

sentence = '他是研究生物化学的'
user_dict = ['他','是','研究','研究生','生物','物化','化学','生物化学','学','的']

FMM_func(user_dict, sentence)
print()
BMM_func(user_dict, sentence)

# 他/是/研究生/物化/学/的/
# 他/是/研究/生物化学/的/
# 非字典词：正向(0)=逆向(0)（越少越好）
# 单字字典词：正向(4)>逆向(3)（越少越好）
# 总词数：正向(6)>逆向(5)（越少越好）
# 因此最终输出为：逆向结果。逆向结果是正确的。
