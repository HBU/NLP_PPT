from FMM import FMM_func
from BMM import BMM_func

sentence = '下雨天留客天留我不留'
user_dict = ['下','雨','下雨','雨天','天','留客','我','不','不留','留']

FMM_func(user_dict, sentence)
print()
BMM_func(user_dict, sentence)

