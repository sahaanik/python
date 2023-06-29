import timeit

t = (1,2,3,4,5)
t2 = ([1,2,3],4,5,6)
t2[0].append(2)
a,b,c = (20,19,39)
print(a,b,c)
print((t2))

print(t[0:3])

print(timeit.timeit('x = (1,2,3,4,5)' , number = 100000))
print(timeit.timeit('x = [1,2,3,4,5]' , number = 100000))