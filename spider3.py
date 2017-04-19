import urllib.request
import re
import os

 


###############################################################################
def func(param):
	fp1 = open("baidu.html", 'wb');
	response = urllib.request.urlopen('http://www.baidu.com/')  
	html = response.read()  
	#print(html)
	fp1.write(html)
	fp1.close()

###############################################################################
def main():
	#call func
	func("aaa")

if __name__ == "__main__":
	main()
###############################################################################



