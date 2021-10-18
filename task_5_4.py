"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
"""
from time import perf_counter

# вариант 1
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 15]
start = perf_counter()
results = []
for i in range(len(src) - 1):
    if src[i + 1] > src[i]:
        results.append(src[i + 1])
print(results, perf_counter() - start)

# вариант 2
start = perf_counter()
results = [src[i + 1] for i in range(len(src) - 1) if src[i + 1] > src[i]]
print(results, perf_counter() - start)
