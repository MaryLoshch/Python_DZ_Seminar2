# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму чисел x и y = '))
p = int(input('Введите произведение чисел x и y = '))
x = 1
while x <= 1000:
    if p % x == 0:
        y = p//x
        if x+y == s:
            print(f'Загаданные числа {x} и {y}')
    x += 1
