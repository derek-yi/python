# coding=utf-8

import os
import sys
import time
import re
import shutil



class CLASS_WALK_FILE:
    def __init__(self, max_size=1024):
        self.m_max_size = max_size
        self.m_log_fp = open("dir_sync.txt", 'w')

    def set_src_path(self, src_path):
        self.m_src_path = src_path

    def set_dst_path(self, dst_path):
        self.m_dst_path = dst_path

    def set_file_filter(self, file_filter):
        self.m_file_filter = file_filter
        
    def show_file_info(self, src_file):
        sp = os.path.split(src_file)
        print(sp[0], sp[1])
        print("size:", os.path.getsize(src_file))
        print("created:", time.ctime(os.path.getctime(src_file)))
        print("modified:", time.ctime(os.path.getmtime(src_file)))

    def file_need_copy(self, src_file, dst_file):
        suffix = os.path.splitext(src_file)[-1]
        #print("suffix ", src_file, suffix, self.m_file_filter)
        if suffix in self.m_file_filter:
            return 0
        if os.path.exists(dst_file) == False:
            return 1
        if os.path.getsize(src_file) != os.path.getsize(dst_file):
            log_info = "\n differ file size %s"%(src_file)
            self.m_log_fp.write(log_info)
            return 1
        
    def copy_file(self, src_file, dst_file):
        sp = os.path.split(dst_file)
        if os.path.exists(sp[0]) == False:
            os.makedirs(sp[0])
        if self.file_need_copy(src_file, dst_file):
            log_info = "\ncopy file %s \n => %s"%(src_file, dst_file)
            self.m_log_fp.write(log_info)
            shutil.copy(src_file, dst_file)

    def handle_file1(self, src_file):
        if os.path.getsize(src_file) < self.m_max_size:
            return
        #strinfo = re.compile(self.m_src_path)
        #dst_file = strinfo.sub(self.m_dst_path, src_file)
        dst_file = src_file.replace(self.m_src_path, self.m_dst_path)        
        #self.show_file_info(src_file)
        self.copy_file(src_file, dst_file)
            
    def walk_file1(self, src_path=0):
        if src_path == 0:
            src_path = self.m_src_path
        list = os.listdir(src_path)
        print("walk_file1 handle dir ", src_path)
        log_info = "\nwalk_file1 handle dir %s"%(src_path)
        self.m_log_fp.write(log_info)
        for fi in list:
            filepath = os.path.join(src_path,fi)
            if os.path.isdir(filepath):
                self.walk_file1(filepath)
            else:
                self.handle_file1(filepath)

    def handle_file2(self, dst_file):
        src_file = dst_file.replace(self.m_dst_path, self.m_src_path)        
        #self.show_file_info(src_file)
        if os.path.exists(src_file) == False:
            #print("delet file ", dst_file)
            log_info = "\n delete file %s"%(dst_file)
            self.m_log_fp.write(log_info)
            os.remove(dst_file)
        
    def walk_file2(self, dst_path=0):
        if dst_path == 0:
            dst_path = self.m_dst_path
        list = os.listdir(dst_path)
        print("walk_file2 handle dir ", dst_path)
        log_info = "\nwalk_file2 handle dir %s"%(dst_path)
        self.m_log_fp.write(log_info)
        for fi in list:
            filepath = os.path.join(dst_path,fi)
            if os.path.isdir(filepath):
                self.walk_file2(filepath)
            else:
                self.handle_file2(filepath)

                
my_class = CLASS_WALK_FILE(10*1000)

filter_list = [".exe", ".bin"]
my_class.set_file_filter(filter_list)

#my_class.set_src_path("D:\\06_code\\python")
#my_class.set_dst_path("E:\\06_code\\python")

my_class.set_src_path("F:\\07_ebook\\vdisk")
my_class.set_dst_path("\\\\192.168.31.1\\文档\\vdisk")

#if not exist in src or differ from src, copy to dst
my_class.walk_file1() 

#if not exist in src, delete dst
my_class.walk_file2() 






