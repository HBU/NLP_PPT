import jieba.posseg as pseg
words = pseg.cut("老师说衣服上除了校徽别别别的")
for word, flag in words:
    print('%s %s' % (word, flag))