lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# 1-й способ (он же "колхозный")
print(f'{lst[0]} "{int(lst[1]):02d}" {lst[2]} "{lst[3]}" {lst[4]} '
      f'{lst[5]} {lst[6]} {lst[7]} "+{int(lst[8]):02d}" {lst[9]}')

# 2-й способ (он же "полуколхозный из будущего")
lst_1 = []
for i in lst:
    try:
        i = int(i)
        if i - 9 < 0:
            i = str(i)
            i = '"' + '0' + i[:] + '"'
        else:
            i = str(i)
            i = '"' + i[:] + '"'
        lst_1.append(i)
    except ValueError:
        lst_1.append(i)
lst_1[-2] = '"+05"'
print(*lst_1)

# 3-й способ (он же "рожденный в 2-хдневных муках")
lst_new = []
for i in lst:
    if ord(i[0]) in range(43, 46):
        i = i[0] + '0' + i[1]
    elif ord(i[0]) in range(53, 58):
        i = '0' + i[0]
    lst_new.append(i)

for i in lst_new:
    if ord(i[0]) in range(43, 58):
        # можно через последний символ элемента i[-1], тогда будет range(48, 58), но так затрагиваем и '+' и '-'
        lst_new.insert(lst_new.index(i) + 1, '"')
lst_new.reverse()
for i in lst_new:
    if ord(i[0]) in range(43, 58):
        lst_new.insert(lst_new.index(i) + 1, '"')
lst_new.reverse()

for i in range(len(lst_new)):
    word = lst_new[i]
    word_prev = lst_new[i-1]
    if i == len(lst_new) - 1:
        word_next = None
    else:
        word_next = lst_new[i+1]

    if word_prev == '"' and ord(word[0]) in range(43, 58) or word == '"' and ord(word_next[0]) in range(43, 58):
        print(lst_new[i], end='')
    else:
        print(lst_new[i], end=' ')
