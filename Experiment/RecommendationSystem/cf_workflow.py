# -*- coding: utf-8 -*-
import time
import os
import sys
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from RecommendationSystem.cf import UserCf

assert os.path.exists('RecommendationSystem/data/ratings.csv'), \
    'File not exists in path, run preprocess.py before this.'
print('Start...')
start = time.time()
movies = UserCf().calculate()
for movie in movies:
    print(movie)
print('Cost time: %f' % (time.time() - start))
