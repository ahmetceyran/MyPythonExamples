def f0(x):
    def g0(y):
        return y**3+3
    return g0(x) **4+4
x=f0(1)
print(x)
