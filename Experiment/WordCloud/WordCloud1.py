# 1号词云：《葛底斯堡演说》黑色背景词云（4行代码上手）
# B站专栏：同济子豪兄 2019-5-23

import wordcloud
w = wordcloud.WordCloud()
w.generate('and that government of the people, by the people, for the people, shall not perish from the earth.')
w.to_file('WordCloud/output1.png')