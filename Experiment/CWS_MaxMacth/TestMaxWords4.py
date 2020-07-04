from FMM import FMM_func
from BMM import BMM_func

sentence = '南京市长江大桥'
user_dict = ['南京','南京市','市','市长','长江','大桥','江大桥']

FMM_func(user_dict, sentence)
print()
BMM_func(user_dict, sentence)

# 南京市/长江/大桥/
# 南京/市长/江大桥/
# 非字典词：正向(0)=逆向(0)（越少越好）
# 单字字典词：正向(0)=逆向(0)（越少越好）
# 总词数：正向(3)=逆向(3)（越少越好）
# 因此最终输出为：不确定。正向结果是正确的。