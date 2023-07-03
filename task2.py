# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

import re

TOP = 10
text_count = dict()
sorted_text_count = {}

text = input('Введите текст: ')
text_lst = re.sub(r'\W', ' ', text).upper().split()

for i in range(len(text_lst)):
    text_count[text_lst[i]] = text_lst.count(text_lst[i])

sorted_val = sorted(text_count.values(), reverse=True)

for j in sorted_val:
    for i in text_count.keys():
        if text_count[i] == j:
            sorted_text_count[i] = text_count[i]

while len(sorted_text_count) > TOP:
    sorted_text_count.popitem()
print('TOP-10:')
print(sorted_text_count)
