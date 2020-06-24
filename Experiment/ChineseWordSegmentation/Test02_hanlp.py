# 如果遇到Visual C++ 14.0 is required的问题，https://blog.csdn.net/qq_38161040/article/details/88203864
# jpype1 缺少，也属于上面的问题。大坑，耽误功夫。 2020.6.24 By David。
# 下载模型时间较长，需要耐心 C:\Users\David\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyhanlp\static
from pyhanlp import *
content = "我来到河北保定河北大学上学"
print(HanLP.segment(content))