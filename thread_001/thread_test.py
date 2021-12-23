import threading
def action(*add):
    for arc in add:
        #调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() +" "+ arc)

#定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/","http://c.biancheng.net/shell/","http://c.biancheng.net/java/")

thread = threading.Thread(target = action,args = my_tuple)
thread.daemon = True

thread.start()