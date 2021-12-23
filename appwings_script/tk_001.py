import tkinter as tk
from appwings_script.sco_rpc_data_v import des_decrypt

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('PD解密脚本')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('600x410')  # 这里的乘是小x

def b_print():
    index = lb.get(lb.curselection())
    list1 = {'S1': 'SSO','S2': 'ERP','S3': 'CRM','S4': 'NC','S5': 'OA','S6': 'Mall','S7': 'App','S8': 'Chat','S9': 'UsedCar','S10': 'EHR'}
    a = des_decrypt(list1[index],var_data.get())
    decrypy_data.delete(1.0, "end")
    decrypy_data.insert(tk.INSERT, a)

# 加密数据
tk.Label(window, text='加密数据：', font=('Microsoft YaHei', 14)).place(x=0, y=0)
var_data = tk.StringVar()
entry_data = tk.Entry(window, textvariable=var_data, font=('Arial', 14)).place(x=100,y=3)   #加密数据输入框
b = tk.Button(window, text="解密", command=b_print).place(x=350, y=1)

#选择系统参数
tk.Label(window, text='系统秘钥：', font=('Microsoft YaHei', 14)).place(x=0, y=30)
var2 = tk.StringVar()
var2.set(('S1','S2','S3','S4','S5','S6','S7','S8','S9','S10'))
lb = tk.Listbox(window, listvariable=var2)
lb.place(x=100, y=40)

#解密数据
tk.Label(window, text='解密数据:', font=('Microsoft YaHei', 14)).place(x=0, y=230)
decrypy_data = tk.Text(window, height=10)
decrypy_data.place(x=10, y=260)

# 第6步，主窗口循环显示
window.mainloop()