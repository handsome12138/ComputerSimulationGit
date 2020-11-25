import timeit
print(timeit.repeat(stmt="[i for i in range(1000)]", repeat=2, number=100000))
