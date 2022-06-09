import sys
from time import perf_counter
start = perf_counter()
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res = [num for num in src if src.count(num) == 1]
print(res, sys.getsizeof(res), perf_counter() - start, sep='\n')


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
res_set = set()
second_set = set()
for number in src:
    if number not in second_set:
        res_set.add(number)
    else:
        res_set.discard(number)
    second_set.add(number)
res_src = [number for number in src if number in res_set]
print(res_src, sys.getsizeof(res_src), type(res_set), perf_counter() - start, sep='\n')



