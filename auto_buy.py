import win32print
import win32gui
import win32con
import win32api
import time
import os,sys,signal
import win32process

handle_chrome = win32gui.FindWindow("Chrome_WidgetWin_1","EHR人事管理系统 - Google Chrome")
handle = win32gui.FindWindowEx(handle_chrome,None,"Chrome_RenderWidgetHostHWND","Chrome Legacy Window")
print(handle_chrome,handle)
# win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
# win32gui.SendMessage(handle,win32con.WM_DESTROY)
# win32gui.SendMessage(handle,win32con.WM_NCDESTROY)
# win32gui.SendMessage(handle,win32con.WM_SHOWWINDOW,True,0)
# win32gui.SendMessage(handle,win32con.WM_CHILDACTIVATE)
# win32gui.SendMessage(handle,win32con.WM_DESTROY)
# win32gui.SendMessage(handle,win32con.WM_NCDESTROY)


position1 = win32api.MAKELONG(1566, 895)
position2 = win32api.MAKELONG(1260,828)
position3 = win32api.MAKELONG(306,75)


# win32gui.SendMessage(handle,win32con.WM_NCHITTEST,None,position1)
# win32gui.SendMessage(handle,win32con.WM_MOUSEACTIVATE,win32con.HTCLIENT,win32gui.W)
# # win32gui.SendMessage(handle,win32con.WM_SETCURSOR,win32con.HTCLIENT,win32con.WM_LBUTTONDOWN)
# win32gui.PostMessage(handle,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,position2)
# win32gui.PostMessage(handle,win32con.WM_MOUSELEAVE)
#
# # win32gui.SendMessage(handle,win32con.WM_NCHITTEST,position1)
# # win32gui.SendMessage(handle,win32con.WM_SETCURSOR,win32con.HTCLIENT,win32con.WM_LBUTTONDOWN)
# win32gui.PostMessage(handle,win32con.WM_MOVE,None,position2)
# win32gui.PostMessage(handle,win32con.WM_MOUSELEAVE)

# win32gui.SetWindowPos(handle,win32con.HWND_BOTTOM,0,0,0,0,win32con.SWP_HIDEWINDOW)

# thread,processId =win32process.GetWindowThreadProcessId(handle)
# os.kill(processId,signal.CTRL_C_EVENT)
# # os.kill(processId,signal.CTRL_BREAK_EVENT)
#
# win32gui.SendMessage(handle,win32con.WM_SHOWWINDOW)
#
#
# win32gui.SendMessage(handle,win32con.WM_MOVE,None,position3)
# win32gui.SendMessage(handle,win32con.WM_WINDOWPOSCHANGED,None,None)
#
# win32gui.SendMessage(handle,win32con.WM_CHILDACTIVATE)
# win32gui.SendMessage(handle,0x0090)
# win32gui.SendMessage(handle,win32con.WM_DESTROY)


win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, position2)
win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, position2)