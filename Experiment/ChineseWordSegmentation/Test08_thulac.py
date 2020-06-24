# 清华
# THULAC需要分词和词性标注模型的支持，获取下载好的模型用户可以登录thulac.thunlp.org网站填写个人信息进行下载，
# 并放到THULAC的根目录即可，或者使用参数model_path指定模型的位置。

# (需要填写信息下载模型，有点麻烦，暂时放弃)
import thulac	

thu1 = thulac.thulac()  #默认模式
text = thu1.cut("我爱北京天安门", text=True)  #进行一句话分词
print(text)
