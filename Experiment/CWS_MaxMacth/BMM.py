def BMM_func(user_dict, sentence):
    """
    反向最大匹配（BMM）
    :param user_dict:词典
    :param sentence:句子
    """
    
    max_len = max([len(item) for item in user_dict]) # 词典中最长词长度
    result = []
    start = len(sentence)
    #print("start:"+str(start))
    #print("max_len:"+str(max_len))
    while start != 0:
        index = start - max_len
        #print("start:"+str(start))
        #print("max_len:"+str(max_len))
        #print("index:"+str(index))
        if index < 0: # 如果最大词出了界线，从边界开始算
            index = 0
            #break
        for i in range(max_len):
            if (sentence[index:start] in user_dict) or (len(sentence[start:index])==1):
                result.append(sentence[index:start])
                start = index
                break
            index += 1

    for i in result[::-1]:
        print(i, end='/')
