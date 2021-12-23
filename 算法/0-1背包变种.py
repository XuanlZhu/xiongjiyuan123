a=[[260,5],[360,4],[230,4],[130,2],[60,1],[160,4]]

sum_money = 3200
sum_num = 60
i = len(a)-1
def price(i):
    return a[i][0]

def value(i):
    return a[i][1]

def f_max_v(sum_num,sum_money,i):
    if sum_num <= 0 or sum_money <= 0:
        return 0
    if i == 0:
        return sum_num*value(0)
    max_v = 0
    for j in range(sum_num+1):
        max_v = max(max_v,f_max_v(sum_num-j,sum_money-j*price(i),i-1)+j*value(i))
    return max_v


print(f_max_v(sum_num,sum_money,i))
