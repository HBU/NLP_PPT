# 如果遇到Visual C++ 14.0 is required的问题，https://blog.csdn.net/qq_38161040/article/details/88203864
# jpype1 缺少，也属于上面的问题。大坑，耽误功夫。 2020.6.24 By David。
# 下载模型时间较长，需要耐心。可以自己单独下载后，拷贝到相关文件夹。 
# 找不到Java，请安装JDK8：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
# 配置java环境：https://www.runoob.com/w3cnote/windows10-java-setup.html
# 注意：各种都要统一。安装一致的Java、Python、JPype1（必须都为32位或64位）。
# 2020.6.24 hanLP在笔记本上正常使用。 一路也是踩坑无数。

from pyhanlp import *
content = "保定市长江大桥"
print(HanLP.segment(content))