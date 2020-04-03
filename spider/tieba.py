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
        self.siteURL = 'http://tieba.baidu.com/p/2460150866'
        self.index = 0
        self.dir = dir
        if os.path.exists(dir):
            shutil.rmtree(dir) 	
        #os.rmdir(dir)
        os.mkdir(dir)

# 翻页的地址规则：view-source:https://tieba.baidu.com/p/2460150866?pn=1
# pn后面是页码
    def getPage(self,pageIndex):
        url = self.siteURL + "?pn=" + str(pageIndex)
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')

# 网页代码中图片的代码为：
# src="https://imgsa.baidu.com/forum/w%3D580/sign=294db374d462853592e0d229a0ee76f2/e732c895d143ad4b630e8f4683025aafa40f0611.jpg" pic_ext="bmp"  height="328" width="560">
# src="https://imgsa.baidu.com/forum/w%3D580/sign=114c0f68b58f8c54e3d3c5270a282dee/3d4e78f0f736afc3c72cf6e3b219ebc4b7451211.jpg" pic_ext="jpeg"  height="373" width="560">
# 所有图片：reg = r'src="(.+?\.jpg)" pic_ext'
# 只看jpg：reg = r'src="(.+?\.jpg)" pic_ext=“jpeg”'
# 要求高度和宽度：reg = r'src="(.+?\.jpg)" pic_ext=“jpeg” height="[5-9][0-9][0-9]"'
# 		
    def getAllImg(self,page):
        #从代码中提取图片
        reg = r'src="(.+?\.jpg)" pic_ext'
        #reg = r'src="(.+?\.jpg)" pic_ext=“jpeg”'
        #reg = r'src="(.+?\.jpg)" pic_ext=“jpeg” height="[2-9][0-9][0-9]"'
        patternImg = re.compile(reg)
        #patternImg = re.compile('src="(.+?\.jpg)" pic_ext',re.S)
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
            #print(imageURL)
            u = urllib.request.urlopen(imgurl)
            data = u.read()
            filename = "%d.jpg" % self.index
            self.saveOnePic(filename, data)
            self.index += 1  
        
    def savePageInfo(self,pageIndex):
        pageinfo = self.getPage(pageIndex)
        imglist = self.getAllImg(pageinfo)
        self.saveImglist2(imglist)

    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print("self.savePageInfo",i)
            self.savePageInfo(i)


#传入起止页码即可
spider = Spider(r"D:\code\python\tieba")
spider.savePagesInfo(1,3)


