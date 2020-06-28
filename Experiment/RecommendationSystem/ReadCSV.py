import csv 

csv_file=csv.reader(open('RecommendationSystem/data/movies.csv','r', encoding='UTF-8'))

for line in csv_file:
    print(line) #打印文件每一行的信息
    
