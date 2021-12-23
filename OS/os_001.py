import os

ret=os.access(r'C:\Users\cpr247\Desktop\系统整理',os.F_OK)  #检查目标文件权限
print(ret)

