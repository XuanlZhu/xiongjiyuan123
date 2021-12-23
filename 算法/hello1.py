a=[[800,2,0],[400,5,1],[300,5,1],[400,3,0],[500,2,0]]
a = [[20,3,5],[20,3,5],[10,3,0],[10,2,0],[10,1,0]]
a = [[300,5,0],[400,2,0],[300,5,2],[300,4,2],[600,4,0]]
a = [[800,2,0],[400,5,1],[200,5,1],[400,3,0],[500,2,0]]

for i in range(len(a)):
    a[i].append(i)

a.sort(reverse=True,key=lambda x:x[2])
print(a)
sum_money = 1000
sum_num = 5
i = len(a)-1
def price(i):
    return a[i][0]

def value(i):
    return a[i][1]

def is_main(i):
    return a[i][2]

def pre_index(i):
    return a[i][3]

dic = {}

"""[[400, 5, 1, 1], [200, 5, 1, 2], [800, 2, 0, 0], [400, 3, 0, 3], [500, 2, 0, 4]]"""
def f_max_v(sum_money,i,main=[]):
    if (sum_money,i,tuple(main)) in dic:
        return dic[(sum_money,i,tuple(main))]
    if sum_money <= 0 or i < 0:
        dic[(sum_money,i,tuple(main))] = 0
        return 0
    if sum_money < price(i):
        dic[(sum_money, i-1, tuple(main))] = f_max_v( sum_money, i - 1, main)
        return dic[(sum_money, i-1, tuple(main))]
    if is_main(i)==0:
        '''如果是主件，可以自由判断是否购买'''
        dic[(sum_money-price(i),i-1,tuple(main+[pre_index(i)]))] = f_max_v(sum_money-price(i),i-1,main+[pre_index(i)])
        dic[(sum_money,i-1,tuple(main))] = f_max_v(sum_money,i-1,main)
        max_v = max(dic[(sum_money-price(i),i-1,tuple(main+[pre_index(i)]))]+price(i)*value(i),f_max_v(sum_money,i-1,main))
        return max_v
    else:
        '''如果是配置，先判断主件是否购买'''
        if is_main(i)-1 in main:
            '''如果主件已购买，那么配件可以自由判断是否购买'''
            dic[(sum_money - price(i), i - 1, tuple(main))] = f_max_v(sum_money - price(i), i - 1,main)
            dic[(sum_money, i - 1, tuple(main))] = f_max_v(sum_money, i - 1, main)
            max_v = max(dic[(sum_money - price(i), i - 1, tuple(main))] + price(i) * value(i),dic[(sum_money, i - 1, tuple(main))])
            return max_v
        else:
            '''如果主件没有购买，那么配件不能购买'''
            dic[(sum_money, i - 1, tuple(main))] = f_max_v(sum_money, i - 1, main)
            return dic[(sum_money, i - 1, tuple(main))]
print(f_max_v(sum_money,i))