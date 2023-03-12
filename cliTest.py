import sys
import os
import keyboard
import time 
sys.path.append(os.getcwd())

from menu.cliMenu import climenu

list = ["Test","Haho","V","T","ahm","afafafeafa","eafaf"]

t = climenu()
sle = t.xyMenu(3,3,list,True,True,True) 
print(sle)
      
                                     