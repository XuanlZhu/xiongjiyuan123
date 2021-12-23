import random


def create_id_code():
    a = random.randint(11,82)    #省份
    b = random.randint(1000,9999)   #地区
    c = random.randint(18,19)       #年前两位
    d = random.randint(10,99)       #年后两位
    e = ['01','02','03','04','05','06','07','08','09','10','11','12']
    e_2 = e[random.randint(0,11)]   #月
    f = random.randint(10,27)   #日
    g = random.randint(10,99)
    h = random.randint(0,1)

    id =str(a)+str(b)+str(c)+str(d)+str(e_2)+str(f)+str(g)+str(h)
    factor = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    S = 0
    for i in range(len(id)):
        S = S + int(id[i])*factor[i]

    index = S%11
    ckcodes = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    code = ckcodes[index]
    id = id+code


    print(id)
    return id


if __name__ == '__main__':
    create_id_code()