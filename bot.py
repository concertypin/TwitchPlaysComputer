import time

import pyautogui as pyautogui
import sys


class KeyIsStr(Exception):
    def __init__(self):
        super().__init__("Key Up/Down with str is not acceptable")


"""
def MakeKeyPress(key, flag=None, delay=0):
    if (len(key) != 1 and flag is not None):
        raise KeyIsStr
    time.sleep(1)
    if (flag == True):
        # 누르기만 하기
        pyautogui.keyDown(key)

    elif (flag == False):
        # 떼기만 하기
        pyautogui.keyUp(key)
    
    elif (flag is None and len(key) != 1):
        # 긴 문장 입력
        pyautogui.write(key, interval=delay)
    else:
        # 눌렀다 떼기
        pyautogui.press(key, interval=delay)
"""

def GetScrollLock():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x91
    return hllDll.GetKeyState(VK_CAPITAL)

def MakeKeyPress(key, delay=0):
    time.sleep(1)
    if (len(key) != 1):
        pyautogui.write(key, interval=delay)
    else:
        pyautogui.press(key, interval=delay)


def main(command):
    if(GetScrollLock()==1):
        return
    print("python got " + command)
    if (command[:1] != "#"):  # 명령어 아니면 정지
        return
    if (command.isalpha() == False):  # 영어 아니면 정지
        return

    cmd = command[1:]  # 명령어 다듬기
    print("->" + cmd, end="")  # 채팅 받음
    MakeKeyPress(cmd)  # 버튼 진짜로 누르기
    print(", pressed", cmd)  # 리턴


if __name__ == "__main__":
    main(sys.argv[1])
