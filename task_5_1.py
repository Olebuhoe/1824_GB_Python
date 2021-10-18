"""
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
"""


def nums_gen(number):
    for _ in range(1, number + 1, 2):
        yield _


n = nums_gen(7)
print(next(n))
print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
