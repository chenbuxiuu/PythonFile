
# def f(a):
#     return abs(a)

def PositiveIntegerAdd(a,b,f):
    if isinstance(a,int) and isinstance(b,int):
        return f(a)+f(b)
