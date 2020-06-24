# pip install pyttsx3
# pip install pywin32

import pyttsx3

Teacher = pyttsx3.init()
Teacher.say('Hello World! 你好，世界！')
Teacher.runAndWait()