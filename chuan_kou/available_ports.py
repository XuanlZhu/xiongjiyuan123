import serial #导入模块
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
for i in port_list:
    print(i)