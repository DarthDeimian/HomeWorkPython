"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3
"""
import random

x = random.randint(0,1000)
y = random.randint(0,1000)
print(f'задуманное первое число ="{x}", второе число ="{y}"')

s = x + y
p = x * y
print(f'сумма чисел ="{s}", произведение чисел ="{p}"')

for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'задуманное первое число ="{x}", второе число ="{y}"')