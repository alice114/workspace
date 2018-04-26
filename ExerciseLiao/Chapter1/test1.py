def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1,3,5,7)
f2 = lazy_sum(1,3,5,7)

f3 = lazy_sum(1,3,5,7,9)

print(f1)
print(f2)
print(f3)
print(f1())




