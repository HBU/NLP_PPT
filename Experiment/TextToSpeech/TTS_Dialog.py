# 他说：“她这个人真有意思。”
# 她说：“他这个人怪有意思的。”
# 于是人们以为他们有了意思，并让他向她意思意思。
# 他火了：“我根本没有那个意思！”
# 她也生气了：“你们这么说是什么意思？”
# 事后有人说：“真有意思。”
# 也有人说：“真没意思”。
import pyttsx3

PersonA = pyttsx3.init()
PersonB = pyttsx3.init()
PersonC = pyttsx3.init()
PersonA.say('“她这个人真有意思。”')
PersonB.say('“他这个人怪有意思的。”')
PersonC.say('于是人们以为他们有了意思，并让他向她意思意思。')
PersonA.say('“我根本没有那个意思！”')
PersonB.say('“你们这么说是什么意思？”')
PersonC.say('事后有人说：“真有意思。”')
PersonC.say('也有人说：“真没意思”。')
PersonA.runAndWait()
PersonB.runAndWait()
PersonC.runAndWait()