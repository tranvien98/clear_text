"""
File tạo từ điển âm vị 
"""
from rules import onsets, nuclei, codas, tones, character
import numpy as np 


"""
tạo ra các vần trong câu
"""

list_word = []
for k in nuclei.keys():
    for j in range(0,6):
        inputt = []
        # inputt.append('@')
        inputt.append(str(nuclei[k]))
        inputt.append(str(j))
        # print(inputt)
        ch = ''.join(inputt)
        # print(ch)
        list_word.append(ch)
num = 0
for k in nuclei.keys():
    for i in codas.keys():
        for j in range(0,6):
            inputt = []
        #     inputt.append('@')
            inputt.append(nuclei[k])
            inputt.append(codas[i])
            inputt.append(str(j))
            ch = ''.join(inputt)
            # print(ch)
            num = num + 1
            list_word.append(ch)

"""
nạp các kí tự trong tiếng anh
"""
for k in character.keys():
    list_word.append(k)
    # print(k)

"""
nạp các kí tự trong tiếng việt
"""
kitu = ['a','ă','â','b','c','d','đ','e','ê','g','h','i','k','l','m','n','o','ô','ơ','p','q','r','s','t','u','ư','v','x','y']
for k in kitu:
    list_word.append(k)
    list_word.append(k.upper())
    # print(k.upper())

"""
nạp âm đầu và lọc từ
"""
for k in onsets.keys():
    list_word.append(onsets[k])
arr_word = np.asarray(list_word)
wo, counts = np.unique(arr_word, return_counts=True)
# print('length:', len(wo))
# print(wo)

"""
Lưu file
"""
f = open('/home/tranvien/speech/deepvoice3/deepvoice3_pytorch/frontend/vi/cmudvi/dictionary.txt', 'w+', encoding='utf-8')

for i in wo:
    # print(i)
    f.writelines(i + '\n')
f.close()