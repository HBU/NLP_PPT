import jieba

test = jieba.cut("赵四是河北大学网络空间安全与计算机学院计科三班的同学") 
print(", ".join(test))
