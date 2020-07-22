#############################################################
# function: max probility segment
# a dynamic programming method
# https://blog.csdn.net/wangliang_f/article/details/17532633
# input: dict file
# output: segmented words, divide by delimiter "\ "
# author: wangliang.f@gmail.com
# edit: update to Python3.8 by David 2020.7.6 
##############################################################
import sys
import math

#global parameter
DELIMITER = " " #分词之后的分隔符

class DNASegment:
    def __init__(self):
        self.word1_dict = {} #记录概率,1-gram
        self.word1_dict_count = {} #记录词频,1-gram
        self.word1_dict_count["<S>"] = 8310575403 #开始的<S>的个数 

        self.word2_dict = {} #记录概率,2-gram
        self.word2_dict_count = {} #记录词频,2-gram


        self.gmax_word_length = 0
        self.all_freq = 0 #所有词的词频总和,1-gram的

    #估算未出现的词的概率,根据beautiful data里面的方法估算
    def get_unkonw_word_prob(self, word):
        return math.log(10./(self.all_freq*10**len(word)))

    #获得片段的概率
    def get_word_prob(self, word):
        #if self.word1_dict.has_key(word): #如果字典包含这个词
        if word in self.word1_dict:
            prob = self.word1_dict[word]
        else:
            prob = self.get_unkonw_word_prob(word)
        return prob

    
    #获得两个词的转移概率
    """
    def get_word_trans_prob(self, first_word, second_word):
        trans_word =  first_word + " " + second_word
        if self.word2_dict.has_key(trans_word):
            trans_prob = self.word2_dict[trans_word]
        else:
            trans_prob = self.get_word_prob(second_word)

        return trans_prob
    """
    def get_word_trans_prob(self, first_word, second_word):
        trans_word =  first_word + " " + second_word
        #print trans_word
        #if self.word2_dict_count.has_key(trans_word):
        if trans_word in self.word2_dict_count:
            trans_prob = \
    math.log(self.word2_dict_count[trans_word]/self.word1_dict_count[first_word])
        else:
            trans_prob = self.get_word_prob(second_word)
        return trans_prob

    """
    #获得转移概率，到segment的
    def get_trans_prob(self, sequence, node, next_segment, prob_sum_list):
        max_seg_length = min([node, self.gmax_word_length])
        pre_node_list = [] #前驱节点列表
        #获得所有的前驱片段，并记录累加概率
        for segment_length in range(1,max_seg_length+1):
            segment_start_node = node-segment_length
            segment = sequence[segment_start_node:node] #获取片段
            pre_node = segment_start_node  #取该片段，则记录对应的前驱节点
            
            trans_prob = self.get_word_trans_prob(segment, next_segment)
            #pre_node_prob_sum = prob_sum_list[pre_node] #前驱节点的概率的累加值
            pre_node_prob_sum = prob_sum_list[node] #前驱节点的概率的累加值
            #当前node一个候选的累加概率值
            candidate_prob_sum = pre_node_prob_sum + trans_prob
            pre_node_list.append((pre_node, candidate_prob_sum))
        #找到最大的候选概率值
        (best_pre_node, best_prob_sum) = max(pre_node_list,key=lambda d:d[1])
        return (best_pre_node, best_prob_sum)
    """

    #寻找node的最佳前驱节点
    #方法为寻找所有可能的前驱片段
    def get_best_pre_node(self, sequence, node, node_state_list):
        #如果node比最大词长小，取的片段长度以node的长度为限
        max_seg_length = min([node, self.gmax_word_length])
        pre_node_list = [] #前驱节点列表
        
        #获得所有的前驱片段，并记录累加概率
        for segment_length in range(1,max_seg_length+1):
            segment_start_node = node-segment_length
            segment = sequence[segment_start_node:node] #获取片段

            pre_node = segment_start_node  #取该片段，则记录对应的前驱节点
            
            if pre_node == 0: 
                #如果前驱片段开始节点是序列的开始节点，
                #则概率为<S>转移到当前词的概率
                #segment_prob = self.get_word_prob(segment)
                segment_prob = \
                        self.get_word_trans_prob("<S>", segment)
            else: #如果不是序列开始节点，按照二元概率计算
                #获得前驱片段的前一个词
                pre_pre_node = node_state_list[pre_node]["pre_node"]
                pre_pre_word = sequence[pre_pre_node:pre_node]
                segment_prob = \
                        self.get_word_trans_prob(pre_pre_word, segment)
            
            pre_node_prob_sum = node_state_list[pre_node]["prob_sum"] #前驱节点的概率的累加值

            #当前node一个候选的累加概率值
            candidate_prob_sum = pre_node_prob_sum + segment_prob 

            pre_node_list.append((pre_node, candidate_prob_sum))

        #找到最大的候选概率值
        (best_pre_node, best_prob_sum) = \
                max(pre_node_list,key=lambda d:d[1])
        return (best_pre_node, best_prob_sum) 

    #最大概率分词
    def mp_seg(self, sequence):
        sequence = sequence.strip()

        #初始化
        node_state_list = [] #记录节点的最佳前驱，index就是位置信息
        #初始节点，也就是0节点信息
        ini_state = {}
        ini_state["pre_node"] = -1 #前一个节点
        ini_state["prob_sum"] = 0 #当前的概率总和
        node_state_list.append( ini_state )
        #字符串概率为2元概率
        #P(a b c) = P(a|<S>)P(b|a)P(c|b)

        #逐个节点寻找最佳前驱节点
        for node in range(1,len(sequence) + 1):
            #寻找最佳前驱，并记录当前最大的概率累加值
            (best_pre_node, best_prob_sum) = \
                    self.get_best_pre_node(sequence, node, node_state_list)
            
            #添加到队列
            cur_node = {}
            cur_node["pre_node"] = best_pre_node
            cur_node["prob_sum"] = best_prob_sum
            node_state_list.append(cur_node)
            #print "cur node list",node_state_list

        # step 2, 获得最优路径,从后到前
        best_path = []
        node = len(sequence) #最后一个点
        best_path.append(node)
        while True:
            pre_node = node_state_list[node]["pre_node"]
            if pre_node == -1:
                break
            node = pre_node
            best_path.append(node)
        best_path.reverse()

        # step 3, 构建切分
        word_list = []
        for i in range(len(best_path)-1):
            left = best_path[i]
            right = best_path[i + 1]
            word = sequence[left:right]
            word_list.append(word)

        seg_sequence = DELIMITER.join(word_list)
        return seg_sequence

    #加载词典，为词\t词频的格式
    def initial_dict(self, gram1_file, gram2_file):
        #读取1_gram文件
        dict_file = open(gram1_file, "r")
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            self.word1_dict_count[key] = value
        #计算频率
        self.all_freq = sum(self.word1_dict_count.values()) #所有词的词频
        self.gmax_word_length = max(len(key) for key in self.word1_dict_count.keys()) 
        self.gmax_word_length = 20
        self.all_freq = 1024908267229.0
        #计算1gram词的概率
        for key in self.word1_dict_count:
            self.word1_dict[key] = math.log(self.word1_dict_count[key]/self.all_freq)
        
        #读取2_gram_file，同时计算转移概率
        dict_file = open(gram2_file, "r")
        for line in dict_file:
            sequence = line.strip()
            key = sequence.split('\t')[0]
            value = float(sequence.split('\t')[1])
            first_word = key.split(" ")[0]
            second_word = key.split(" ")[1]
            self.word2_dict_count[key] = float(value)
            #python3 : if dict.has_key(word):#改为：#if word in dict:            
            if first_word in self.word1_dict_count:
                self.word2_dict[key] = \
                    math.log(value/self.word1_dict_count[first_word])  #取自然对数
            else:
                self.word2_dict[key] = self.word1_dict[second_word]
#test
if __name__=='__main__':
    myseg = DNASegment()
    myseg.initial_dict("CWS_n-gram/count_1w.txt","CWS_n-gram/count_2w.txt")

    sequence = "itisatest"
    seg_sequence = myseg.mp_seg(sequence)
    print("original sequence: " + sequence)
    print("segment result: " + seg_sequence)

    sequence = "hebeiuniversitycollegeofcyberspacesecurityandcomputer"
    seg_sequence = myseg.mp_seg(sequence)
    print("original sequence: " + sequence)
    print("segment result: " + seg_sequence)
