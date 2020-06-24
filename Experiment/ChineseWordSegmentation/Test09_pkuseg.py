# 北大
import pkuseg
seg = pkuseg.pkuseg()				#以默认配置加载模型
text = seg.cut('我来到河北保定河北大学上学')	#进行分词
print(text)