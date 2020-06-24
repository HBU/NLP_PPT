# -*- coding: utf-8 -*-
import time
import requests
import urllib.parse
import urllib.request​​

def fetch_token(): # 提交请求，拿到
token api_key = "0Hyq8G4ClwUlgWNxAKLULGRP" # 使用百度AI平台管理中心中创建的应用的API Key
secret_key = "wC57Q8BetTcFxuGpHlwtVkutdYrwgND8" # 使用百度AI平台管理中心中创建的应用的Secret Key
token_url = "https://openapi.baidu.com/oauth/2.0/token"
print("fetch token begin")
params = {"grant_type": "client_credentials", "client_id": api_key, "client_secret": secret_key}
r = requests.get(url=token_url, params=params)
if r.status_code == 200:
     rstr = r.json() # print(r.status_code)
     # print(rstr) # print(r.text)
     # print(rstr['access_token'])
    tok = rstr['access_token']
     return(tok)
else: print(r.text)
print('请求错误！')​​
""" TOKEN end """​​
if __name__ == '__main__':
    token = fetch_token()
    TTS_URL = "https://tsn.baidu.com/text2audio"
    # text = u"莫听穿林打叶声，何妨吟啸且徐行。竹杖芒鞋轻胜马。谁怕？一蓑烟雨任平生。料峭春风吹酒醒，微冷，山头斜照却相迎。回首向来萧瑟处，归去。也无风雨也无晴。".encode('utf8')
text = u"如今，有关品牌的闲谈远比精准的广告宣传更为可信。社交圈子接过了外部营销交流和个人喜好的火炬，成为影响力的主要来源。用户在选择品牌时倾向于听取朋友的经验，好像在建起一座社交圈子筑成的堡垒，免受虚假品牌宣传和营销手段的欺骗。".encode('utf8')
# 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
# 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美 PER = 106 # 语速，取值0-15，默认为5中语速
SPD = 5 # 音调，取值0-15，默认为5中语调
PIT = 5 # 音量，取值0-9，默认为5中音量
VOL = 5 # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav AUE = 3​
FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]
data = urllib.parse.urlencode({'tex': text, 'per': PER, 'tok': token, 'cuid': '20009514', 'ctp': 1, 'lan': 'zh', 'aue': AUE})
# print('test on Web Browser' + TTS_URL + '?' + data)​
req = requests.post(TTS_URL, data)​print(req.status_code)
if req.status_code == 200:
    # print(req.content)
    result_str = req.content
    save_file = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.' + FORMAT
with open(save_file, 'wb') as of:
    of.write(result_str)
    print('success!')
else: 
    print('has error!')


# 链接：https://www.jianshu.com/p/59c6aa6781a5