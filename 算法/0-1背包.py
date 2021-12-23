a = [5,1,6,5,9]
memo = {}
def f(i):
    if i in memo:
        return memo[i]
    if i == len(a) - 1:
        return 1
    maxl = 1
    for j in range(i+1,len(a)):
        if a[j] >= a[i]:
            maxl = max(maxl,f(j)+1)
    memo[i] = maxl
    return maxl

def lis():
    return max(f(i) for i in range(len(a)))


def lis2():
    n =len(a)   #5
    L = [1] * n

    for i in reversed(range(n)):  # i -> 4,3,2,1,0
        for j in range(i+1,n):
            if a[j] > a[i]:
                L[i] = max(L[i],L[j]+1)
    return max(L)

print(lis2())
