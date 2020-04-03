__author__ = 'derek.yi'
# -*- coding:utf-8 -*-

#import urllib
#import urllib2
import urllib.parse
import urllib.request
import re
import os
import shutil

class Spider:

    #页面初始化
    def __init__(self, dir):
        self.siteURL = 'http://jandan.net/ooxx/'
        self.index = 0
        self.dir = dir
        if os.path.exists(dir):
            shutil.rmtree(dir) 	
        #os.rmdir(dir)
        os.mkdir(dir)

# 翻页的地址规则：http://jandan.net/ooxx/page-5#comments
# page-后面是页码
    def getPage(self,pageIndex):
        url = self.siteURL + "page-%d#comments"%pageIndex
        print(url)
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')

# 网页代码中图片的代码为：
# <img src="//ww3.sinaimg.cn/bmiddle/4c525fcetw1dhgf8jqgosj.jpg" />
# 所有图片：r'img src="(.+?\.jpg)"'
# 		
    def getAllImg(self,page):
        #从代码中提取图片
        reg = r'img src="(.+?\.jpg)"'
        patternImg = re.compile(reg)
        imglist = re.findall(patternImg, page)
        return imglist
		
    def saveOnePic(self, filename, data):
            filename = os.path.join(self.dir, filename)
            f = open(filename, 'wb')
            f.write(data)
            f.close()        	

    #传入图片地址，保存单张图片
    def saveImglist2(self,imglist):
        for imgurl in imglist:
            print(imgurl)
            if not imgurl.startswith('http'):
                imgurl = "http:" + imgurl
            try:
                u = urllib.request.urlopen(imgurl)
                data = u.read()
                filename = "%d.jpg" % self.index
                self.saveOnePic(filename, data)
                self.index += 1  
            except:
                pass
        
    def savePageInfo(self,pageIndex):
        pageinfo = self.getPage(pageIndex)
        imglist = self.getAllImg(pageinfo)
        self.saveImglist2(imglist)

    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print("self.savePageInfo",i)
            self.savePageInfo(i)


#传入起止页码即可
spider = Spider(r"D:\code\python\jiandan")
spider.savePagesInfo(1,30)


