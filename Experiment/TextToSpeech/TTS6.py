# 普通语速，读文章
import pyttsx3

f = open('TextToSpeech/Spring.txt',encoding='utf-8')
msg = f.read()
teacher = pyttsx3.init()
teacher.say(msg)
teacher.runAndWait()