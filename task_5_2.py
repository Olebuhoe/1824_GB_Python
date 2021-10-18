# Наверное это наивно давать такой вариант для задания под *, но это генератор и он без yield

n = 18
nums_gen = (i for i in range(1, n + 1, 2))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
