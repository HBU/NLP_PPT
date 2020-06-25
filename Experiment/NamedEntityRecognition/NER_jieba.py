import jieba
import jieba.posseg as posseg
import re
from datetime import datetime,timedelta
from dateutil.parser import parser
 
 
# 中文词性标注和命名实体识别
sent = "中文分词是文本处理不可或缺的一步！"
seglist = posseg.cut(sent)
# print(seglist)
print(''.join(['{0}/{1}'.format(w, t) for w, t in seglist]))
# 中文/nz分词/n是/v文本处理/n不可或缺/l的/uj一步/m！/x
 
# 日期识别
 
UTIL_CN_NUM = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4,
               '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
               '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
 
UTIL_CN_UNIT = {'十': 10, '百': 100, '千': 1000, '万': 10000}
 
 
def cn2dig(src):
    if src == "":
        return None
    m = re.match("\\d+", src)
    if m:
        return int(m.group(0))
    rsl = 0
    unit = 1
    for item in src[::-1]:
        if item in UTIL_CN_UNIT.keys():
            unit = UTIL_CN_UNIT[item]
        elif item in UTIL_CN_NUM.keys():
            num = UTIL_CN_NUM[item]
            rsl += num * unit
        else:
            return None
    if rsl < unit:
        rsl += unit
    return rsl
 
 
def year2dig(year):
    res = ''
    for item in year:
        if item in UTIL_CN_NUM.keys():
            res = res + str(UTIL_CN_NUM[item])
        else:
            res = res + item
    m = re.match("\\d+", res)
    if m:
        if len(m.group(0)) == 2:
            return int(datetime.datetime.today().year/100)*100 + int(m.group(0))
        else:
            return int(m.group(0))
    else:
        return None
 
 
def parse_datetime(msg):
    if msg is None or len(msg) == 0:
        return None
 
    try:
        dt = parser(msg, fuzzy=True)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        m = re.match(r"([0-9零一二两三四五六七八九十]+年)?([0-9一二两三四五六七八九十]+月)?" 
                     "([0-9一二两三四五六七八九十]+[号日])?([上中下午晚早]+)?"
                     "([0-9零一二两三四五六七八九十百]+[点:\\.时])?"
                     "([0-9零一二三四五六七八九十百]+分?)?([0-9零一二三四五六七八九十百]+秒)?", msg)
        if m.group(0) is not None:
            res = {"year": m.group(1),
                   "month": m.group(2),
                   "day": m.group(3),
                   "hour": m.group(5) if m.group(5) is not None else '00',
                   "minute": m.group(6) if m.group(6) is not None else '00',
                   "second": m.group(7) if m.group(7) is not None else '00',
                   }
 
            params = {}
 
            for name in res:
                if res[name] is not None and len(res[name]) != 0:
                    tmp = None
                    if name == 'year':
                        tmp = year2dig(res[name][:-1])
                    else:
                        tmp = cn2dig(res[name][:-1])
                    if tmp is not None:
                        params[name] = int(tmp)
            target_date = datetime.today().replace(**params)
            is_pm = m.group(4)
            if is_pm is not None:
                if is_pm == u'下午' or is_pm == u'晚上' or is_pm == '中午':
                    hour = target_date.time().hour
                    if hour < 12:
                        target_date = target_date.replace(hour=hour + 12)
            return target_date.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return None
 
 
def check_time_valid(word):
    m = re.match("\\d+$", word)
    if m:
        if len(word) <= 6:
            return None
    word1 = re.sub('[号|日]\\d+$', '日', word)
    if word1 != word:
        return check_time_valid(word1)
    else:
        return word1
 
 
# 时间提取
def time_extract(text):
    time_res = []
    word = ''
    keyDate = {'今天': 0, '明天': 1, '后天': 2}
    for k, v in posseg.cut(text):
        if k in keyDate:
            if word != '':
                time_res.append(word)
                word = (datetime.today() + timedelta(days=keyDate.get(k, 0))).strftime('%Y年%m月%d日')
            elif word != '':
                if v in ['m', 't']:
                    word = word + k
                else:
                    time_res.append(word)
                    word = ''
        elif v in ['m', 't']:
            word = k
    if word != '':
        time_res.append(word)
    result = list(filter(lambda x: x is not None, [check_time_valid(w) for w in time_res]))
    final_res = [parse_datetime(w) for w in result]
    return [x for x in final_res if x is not None]
 
 
text1 = '我要住到明天下午三点'
print(text1, time_extract(text1), sep=':')
# 我要住到明天下午三点:['2019-06-09 03:00:00']
text2 = '预定28号的房间'
print(text2, time_extract(text2), sep=':')
# 预定28号的房间:['2019-06-09 00:00:00']
text3 = '我要从26号下午4点住到11月2号'
print(text3, time_extract(text3), sep=':')
# 我要从26号下午4点住到11月2号:['2019-06-09 00:00:00']
text4 = '我要预订今天到30的房间'
print(text4, time_extract(text4), sep=':')
text5 = '今天30号呵呵'
print(text5, time_extract(text5), sep=':')
# 我要预订今天到30的房间:[]
# 今天30号呵呵:['2019-06-09 00:00:00']