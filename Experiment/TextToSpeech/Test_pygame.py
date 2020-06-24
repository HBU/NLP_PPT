# pygame 测试失败:partially initialized module 'pygame' has no attribute 'mixer' (most likely due to a circular import)
# 文件名不要跟包名一样。。。
import pygame
 
pygame.mixer.init()
#加载音乐
pygame.mixer.music.load("TextToSpeech/Welcome.mp3")
while True:
	#检查音乐流播放，有返回True，没有返回False
	#如果没有音乐流则选择播放
	if pygame.mixer.music.get_busy()==False:
		pygame.mixer.music.play()


