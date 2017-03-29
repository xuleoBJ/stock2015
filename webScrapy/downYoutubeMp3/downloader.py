
#-*-coding:utf-8-*-
import urllib
import os 
from sys import argv,exit,stdout

"""
	这回我们试一试下载一个其他文件例如rar看看能不能
	这回我们增加交互，用过sys.argv来传入url 和 filename

"""
def url_decide(url):
	"""
	把url传进来判断rul是否正确
	url 传进来的,url正确就返filname 用于判断文件类型

	"""
	#判断有没有http字符
	if url.find("http://") == -1:
		print "URL Error"
		exit()  
	#判断是不是http开头字符
	if url.split("://")[0] != "http":
		print "Error URL:Are you forget the head of 'HTTP'?"
		exit()
	filename = url.split("/")[-1]
	down_type = ["html","htm","zip","tar.gz","tar","msi","rar"]
	#判断是不是其中的一种类型，是的话就直接返回结尾文件名，不是默认返回html
	#例如 http://zim-wiki.org/downloads/zim-0.60.tar.gz 我们判断结尾就是tar.gz格式
	for i in down_type:
		if i in filename:
			print "Tpye:" + i
			return filename
	#假如不再上面的类型 list中,我们就认为他是一个网站，例如www.baidu.com	
	return "tmp.html"

def path_exists(filename):
	"""
		判断路径是否正确，如果不存在没有就创建
	"""
	if os.path.exists(filename) == True:
		print "path is ok"
	elif os.path.exists(filename) == False:
		print "no path"
		os.mkdir(filename)

def reporthook(count,block_size,total_size):
	"""
	回调函数
	下载进度现实的函数
	@count 已经下载的数据块的个数 是个数哦
	@block_size 数据会的大小，一般都是多少多少字节哦
	@totol_size 总的文件大小
	
	有了这三个量我们就可以计算进度了哈
	只要totol_size 等于 count * block_size 那就说明下载完毕了

	""" 
	per = (100.0 * count * block_size ) / total_size
	#per就是百分进度了
	
	print "Download Percent: %.2f %%" % per,
	stdout.write("\r")
	#输出进度,保留两个百分点，stdout。write("\r")是每次输出光标回到行首，这样目的为了一行输出进度，print xxx, 逗号在print后面表示不换行

def download(url,filename):
	down_log = urllib.urlretrieve(url,filename,reporthook)
	#reporthook是一个回调函数，就是你传函数名(其实是函数的指针，一个地址),然后它实现里面回调用你函数并传进去三个参数
	print "Your file on : " + down_log[0]

script_name,url,path = argv
#argv是一个list 装了我们python xxx.py xx xxx 时候带的参数 argv[0]就是xxx.py argv[1]是xxx 
print "you input argv is '%s' '%s' '%s' " % (script_name,url,path)
#看一看我们输入的参数

filename = url_decide(url)
#判断url对不对和文件类型

path_exists(path)
#判断路径存在否

download_filename = path + filename
#完整的路径链接文件名字，作为参数传过去
print download_filename

download(url,download_filename)
#开始下载吧
