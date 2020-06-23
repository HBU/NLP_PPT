# ref：https://www.cnblogs.com/djdjdj123/p/12153603.html
# ref：https://www.cnblogs.com/wkfvawl/p/11585986.html
# 安装包：pip install numpy matplotlib pillow wordcloud imageio jieba snownlp itchat -i https://pypi.tuna.tsinghua.edu.cn/simple

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud, STOPWORDS


###当前文件路径
d = path.dirname(__file__)

# Read the whole text.
file = open(path.join(d, 'alice.txt'),'r', encoding='UTF-8').read()
##进行分词
#刚开始是分完词放进txt再打开却总是显示不出中文很奇怪
default_mode =jieba.cut(file)
text = " ".join(default_mode)
alice_mask = np.array(Image.open(path.join(d, "QQ.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")
wc = WordCloud(  
    #设置字体，不指定就会出现乱码,这个字体文件需要下载
    font_path=r'/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',  
    background_color="white",   
    max_words=2000,   
    mask=alice_mask,  
    stopwords=stopwords)  
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "qq_result.jpg"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()