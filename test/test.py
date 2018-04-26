s = 0
l = range(1,21)
def op(x):
    if not isinstance(x,int):
        return;
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r;


s = sum(map(op,l))

op(l)
