__author__ = 'derek.yi'
# -*- coding:utf-8 -*-

#import urllib
#import urllib2
import urllib.parse
import urllib.request
import re
import os

#抓取MM
class Spider:

    #页面初始化
    def __init__(self):
        self.siteURL = 'http://tieba.baidu.com/p/2460150866'
        self.index = 0

    #获取索引页面的内容
    def getPage(self,pageIndex):
        url = self.siteURL + "?pn=" + str(pageIndex)
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')

    def getAllImg(self,page):
        #从代码中提取图片
        reg = r'src="(.+?\.jpg)" pic_ext'
        patternImg = re.compile(reg)
        #patternImg = re.compile('src="(.+?\.jpg)" pic_ext',re.S)
        imglist = re.findall(patternImg, page)
        return imglist

    #传入图片地址，保存单张图片
    def saveImglist(self,imglist):
        for imgurl in imglist:
            print(imgurl)
            filename = "%d.jpg" % self.index
            urllib.request.urlretrieve(imgurl,filename)
            #urllib.request.urlretrieve(imgurl,'%s.jpg' % self.index)
            self.index += 1

    def saveImglist2(self,imglist):
        for imgurl in imglist:
            #print(imageURL)
            u = urllib.request.urlopen(imgurl)
            data = u.read()
            filename = "%d.jpg" % self.index
            f = open(filename, 'wb')
            f.write(data)
            f.close()
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
spider = Spider()
spider.savePagesInfo(1,3)


