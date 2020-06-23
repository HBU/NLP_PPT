# ref：https://www.cnblogs.com/djdjdj123/p/12153603.html
# ref：https://www.cnblogs.com/wkfvawl/p/11585986.html
# 安装包：pip install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple

import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 1.读入txt文本数据
text = open(r'test.txt', "r").read()
#print(text)
# 2.结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
cut_text = jieba.cut(text)
# print(type(cut_text))
# 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
result = " ".join(cut_text)
#print(result)
# 3.生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
# 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
wc = WordCloud(
        # 设置字体，不指定就会出现乱码
        # 设置背景色
        background_color='white',
        # 设置背景宽
        width=500,
        # 设置背景高
        height=350,
        # 最大字体
        max_font_size=50,
        # 最小字体
        min_font_size=10,
        mode='RGBA'
        #colormap='pink'
        )
# 产生词云
wc.generate(result)
# 保存图片
wc.to_file(r"QQ1.png") # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
# 4.显示图片
# 指定所绘图名称
plt.figure("jay")
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
plt.show()