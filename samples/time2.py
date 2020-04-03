# -*- coding: utf-8 -*-

import time, os  
def re_exe(cmd, inc = 60):  
    while True:  
        os.system(cmd);  
        time.sleep(inc)  

re_exe("echo %time%", 5)

