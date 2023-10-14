import cv2 
import pyautogui
import numpy as np
import keyboard as key
print('''Welcome to the screen recorder :
      press s to start and q to quit ''')
file_name=input("The file name you want to save with extension like .mp4 : ")
choice=input("press s to start recording : ")
if choice == 's':
    from win32api import GetSystemMetrics 
    width=GetSystemMetrics(0)
    height=GetSystemMetrics(1)
    dim=(width,height)
    f=cv2.VideoWriter_fourcc(*"XVID")
    output=cv2.VideoWriter(file_name,f,30.0,dim)
    while True:
        img=pyautogui.screenshot()
        frame1=np.array(img)
        frame=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
        output.write(frame)
        if key.is_pressed('q'):
         print("ending the recording ...")
         break
