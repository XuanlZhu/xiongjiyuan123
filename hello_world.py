a =[[3,6],[2,9],[6,9],[12,6],[6,5]]

b = {}

def w(n):
    return a[n][0]
def v(n):
    return a[n][1]


def f(n,s):
    if s <=0 or n<0:
        return 0
    if s<w(n):
        return f(n-1,s)
    else:
        return max(f(n-1,s),v(n)+f(n-1,s-w(n)))

print(f(len(a)-1,16))