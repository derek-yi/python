# coding=utf-8

import os
import sys
import time


class CLASS_WALK_FILE:
    def __init__(self, logfile, max_size):
        self.logfile = logfile
        self.max_size = max_size
        self.fp = open(logfile, 'w')

    def file_handle1(self, path):
        sp = os.path.split(path)
        if os.path.getsize(path) > self.max_size:
            print(sp[0], sp[1])
            print("size:", os.path.getsize(path))
            print("created:", time.ctime(os.path.getctime(path)))
            print("modified:", time.ctime(os.path.getmtime(path)))

    def file_handle2(self, path):
        sp = os.path.split(path)
        if os.path.getsize(path) > self.max_size:
            str = "%s %s %d %s \r\n"%(sp[0],sp[1],os.path.getsize(path),time.ctime(os.path.getctime(path)))
            print(str)
            self.fp.write(str)
            
    def walk_file1(self, path):
        list = os.listdir(path)
        for fi in list:
            filepath = os.path.join(path,fi)
            if os.path.isdir(filepath):
                self.walk_file1(filepath)
            else:
                self.file_handle1(filepath)
		
    def walk_file2(self, path):
        for (dirname, subdir, subfile) in os.walk(path):
        #print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
            #print('[' + dirname + ']')
            for f in subfile:
                self.file_handle2(os.path.join(dirname, f))
        
my_class = CLASS_WALK_FILE("E:\\05_code\\python\\log.xls", 10*1000)
my_class.walk_file2("E:\\05_code\\python")
