from FMM import FMM_func
from BMM import BMM_func

sentence = '商品和服务'
user_dict = ['商品','和','和服','服务']

FMM_func(user_dict, sentence)
print()
BMM_func(user_dict, sentence)

# 商品/和服/务/
# 商品/和/服务/
# 非字典词：正向(0)=逆向(0)（越少越好）
# 单字字典词：正向(1)=逆向(1)（越少越好）
# 总词数：正向(3)>逆向(3)（越少越好）
# 因此最终输出为：不确定。逆向结果是正确的。