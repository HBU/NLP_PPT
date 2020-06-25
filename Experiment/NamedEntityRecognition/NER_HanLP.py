# 《自然语言处理入门》8.4.3 基于角色标注的机构名识别
import os
import sys
# 得到当前根目录
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from pyhanlp import *
from ngram_segment import DijkstraSegment
import pku
from test_utility import test_data_path

EasyDictionary = JClass('com.hankcs.hanlp.corpus.dictionary.EasyDictionary')
NTDictionaryMaker = JClass('com.hankcs.hanlp.corpus.dictionary.NTDictionaryMaker')
Sentence = JClass('com.hankcs.hanlp.corpus.document.sentence.Sentence')
MODEL = test_data_path() + "/ns"


def train(corpus, model):
    dictionary = EasyDictionary.create(HanLP.Config.CoreDictionaryPath)  # 核心词典
    maker = NTDictionaryMaker(dictionary)  # 训练模块
    maker.train(corpus)  # 在语料库上训练
    maker.saveTxtTo(model)  # 输出HMM到txt


def load(model):
    HanLP.Config.PlaceDictionaryPath = model + ".txt"  # data/test/ns.txt
    HanLP.Config.PlaceDictionaryTrPath = model + ".tr.txt"  # data/test/ns.tr.txt
    segment = DijkstraSegment().enableOrganizationRecognize(True).enableCustomDictionary(False)  # 该分词器便于调试
    return segment


def test(model=MODEL):
    segment = load(model)
    HanLP.Config.enableDebug()
    #print(segment.seg("温州黄鹤皮革制造有限公司是由黄先生创办的企业"))
    print(segment.seg("江大桥在河北省保定市七一东路2666号河北大学网络空间安全与计算机学院工作"))


if __name__ == '__main__':
    train(pku.PKU199801, MODEL)
    test(MODEL)
