# coding=gbk
from PIL import ImageGrab
import win32gui


def catch(arg):
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    window = [(hwnd, title) for hwnd, title in winlist if arg in title.lower()]
    window = window[0]
    hwnd = window[0]

    try:
        win32gui.SetForegroundWindow(hwnd)
    except:
        print(window[1],hwnd)
        print("126")
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    img.save('a.jpg')


if __name__ == '__main__':
    arg = input()
    catch(arg)