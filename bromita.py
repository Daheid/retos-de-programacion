import pyautogui as pt 
import time


limit = 50
message = "!wa"
imagen = "guerra.jpeg"
i= 0

time.sleep(1)
while i < limit:
    pt.typewrite(message)
    
    pt.press("enter")
    i +=1






























