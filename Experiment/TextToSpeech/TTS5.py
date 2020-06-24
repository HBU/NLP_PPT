# 变换声音
# https://www.jianshu.com/p/0b4c9e9931f5

import pyttsx3

# msg = '''盼望着，盼望着，东风来了，春天的脚步近了...''' # 中文只有一种声音，可能是系统的事儿。 David 2020.6.24

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(len(voices))
for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('I will always love you ')
    engine.runAndWait()


