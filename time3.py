#这里需要引入三个模块
import time, os, sched  

schedule = sched.scheduler(time.time, time.sleep)  
   
def perform_command(cmd, inc):  
    os.system(cmd)  

def timming_exe(cmd, inc = 60):  
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动  
    schedule.enter(inc, 0, perform_command, (cmd, inc))  
    # 持续运行，直到计划时间队列变成空为止  
    schedule.run()  

print("show time after 10 seconds:")  
timming_exe("echo %time%", 10)

