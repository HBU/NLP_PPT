# https://blog.csdn.net/weixin_42365530/article/details/103915056

from aip import AipSpeech	# 导入api接口
from playsound import playsound	# 音频模块

""" 你自己的 APPID AK SK """
APP_ID = '20570364'
API_KEY = '0Hyq8G4ClwUlgWNxAKLULGRP'
SECRET_KEY = 'wC57Q8BetTcFxuGpHlwtVkutdYrwgND8'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

with open('TextToSpeech/Spring1.txt',encoding='utf-8') as f:
    data = f.read()

print(data)
''''per': 4  发声人选择，0为女声,1为男声,3为情感合成-度逍遥,4为情感合成-度丫丫，默认为普通女'''

msg = '吹面不寒杨柳风'

result = client.synthesis(msg, 'zh', 1, {
    'per': 4,
    'spd': 3,  # 速度
    'vol': 7   # 音量
})

if not isinstance(result, dict):
    with open('TextToSpeech/test.wav', 'wb') as f:
        f.write(result)


# 播放。这个函数执行不了，大坑。研究了一下午，未找到解决方案。
# playsound("TextToSpeech/Welcome.mp3")

