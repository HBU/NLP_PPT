# https://blog.csdn.net/ykf173/article/details/105592832

# Author: Kaifeng Yan # Last update: 2020.04.19 # First create: 2020.04.19 
# Edit: David 2020.08.13 


import json
import time
import jieba
import pyhanlp
import pkuseg
import thulac
from snownlp import SnowNLP
import pynlpir
import sys
import os


def mk_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def cal_score(script_score, gold_training_file, gold_test_file, segment_file, out_file):
    command_folder_list = ['perl', script_score, gold_training_file, gold_test_file, segment_file,'>', out_file ]
    command = ' '.join(command_folder_list)
    print(command)
    os.system(command)


class Segment:
    def jieba_segment(self, sentence):
        seg_list = jieba.cut(sentence, cut_all=False)
        sentence = ' '.join(seg_list)
        return sentence

    def hanlp_segment(self, han_tokenizer, sentence):
        # hanlp分词
        sentence = han_tokenizer(sentence)
        return ' '.join(sentence)

    def thulac_segment(self, thu, sentence):
        # thulac 分词
        sentence = thu.cut(sentence, text=True)  # 进行一句话分词
        # cut_f(输入文件, 输出文件)
        return ' '.join(sentence)

    def pkuseg_segment(self, sentence):
        seg = pkuseg.pkuseg(postag=False)  # 以默认配置加载模型
        sentence = seg.cut(sentence)  # 进行分词
        return ' '.join(sentence)

    def pynlpir_segment(self, sentence):
        # pynlpir分词
        pynlpir.open()
        sentence = pynlpir.segment(sentence, pos_tagging=False)
        pynlpir.close()
        return ' '.join(sentence)

    def snownlp_segment(self, sentence):
        # snownlp分词
        # unicode_sentence = sentence.decode('gbk')
        sentence = SnowNLP(sentence).words
        return ' '.join(sentence)


if __name__ == '__main__':
    segment_list = ['hanlp', 'jieba', 'snownlp', 'pynlpir', 'pkuseg', 'thulac']
    data_list = ['cityu', 'as', 'msr', 'pku']
    #   data = dict(zip(data_list, data_list))
    segment_tool = 'jieba'
    data = 'pku'

    if data not in data_list or segment_tool not in segment_list:
        print('ERROR the parameters')
        print("python argv[1]->[hanlp,jieba,snownlp,nlpir,pkuseg,thulac] argv[2]->[cityu, as, msr, pku]")
        exit()

    test_path = 'data/icwb2/testing/' + data + '_test.utf8'
    seg_dir = 'data/icwb2/segment/' + segment_tool + '/' 
    seg_path = seg_dir + data + '_segment_test.utf8'
    gold_training_file = 'data/icwb2/gold/' + data + '_training_words.utf8'
    gold_test_file = 'data/icwb2/gold/' + data + '_test_gold.utf8'
    script_score = 'data/icwb2/scripts/score'
    score_path = 'data/score/' + segment_tool + '/'
    score_file = score_path + data + '_score'
    time_statistic_dir = 'data/time_statistic/'
    time_statistic_path = time_statistic_dir + segment_tool + '_time_statistic.txt'

    mk_dir(seg_dir)
    mk_dir(time_statistic_dir)
    mk_dir(score_path)

    # eval('test_path' + sys.argv[2])字符串转变量
    # eval('seg_path' + sys.argv[2])

    print('test_path=', test_path)
    print('segment_path=', seg_path)

    # if segment_tool == 'jieba':
    #     jieba.enable_paddle()  # 启动paddle模式。 0.40版之后开始支持，早期版本不支持

    segment_func = segment_tool + '_segment'
    start = time.perf_counter()

    if 'thulac' in segment_func:
        thu = thulac.thulac(seg_only=True)
    if 'hanlp' in segment_func:
        han_tokenizer = hanlp.load('PKU_NAME_MERGED_SIX_MONTHS_CONVSEG')
    with open(test_path, 'r', encoding='utf-8-sig') as f_r:  ##注意，这里的编码，utf-8 bom会在文件头加\ufeff，否则会有小问题
        with open(seg_path, 'w', encoding='utf-8') as f_w:
            for line_sentence in f_r:
                if 'thulac' in segment_func:
                    line_sentence = getattr(Segment(), segment_func)(thu, line_sentence)  # 根据参数调用不同分词工具
                elif 'hanlp' in segment_func:
                    line_sentence = getattr(Segment(), segment_func)(han_tokenizer, line_sentence)
                else:
                    line_sentence = getattr(Segment(), segment_func)(line_sentence)  # 根据参数调用不同分词工具
                if 'snow' in segment_func:
                    f_w.write(line_sentence + '\n')
                else:
                    f_w.write(line_sentence)
    end = time.perf_counter()

    with open(time_statistic_path, 'a', encoding='utf-8') as f_time:
        print('分词运行时间：', end - start)
        dic = {}
        dic[test_path[11:-10]] = end - start
        f_time.write(json.dumps(dic) + '\n')

print('start scoring','------'*3)
#to calculate score
cal_score(script_score,gold_training_file, gold_test_file, seg_path, score_file)