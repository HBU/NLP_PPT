# 北大
import pkuseg
seg = pkuseg.pkuseg()				#以默认配置加载模型
text = seg.cut('我爱北京天安门')	#进行分词
print(text)