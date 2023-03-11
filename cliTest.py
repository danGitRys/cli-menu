import sys
import os
sys.path.append(os.getcwd())

from menu.cliMenu import climenu

list = ["Test","Haho","V","T","ahm"]

t = climenu()
t.xyMenu(3,4,list,True,True)