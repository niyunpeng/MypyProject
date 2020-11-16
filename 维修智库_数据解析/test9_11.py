#解析XML，遍历描述.dita文件，进行解析
import time
import re
import os
import os.path
import xml.dom.minidom
import re
from xml.dom.minidom import parse


plist=[]
for filepath,dirnames,filenames in os.walk(r'E:\数字化部\算法中心\维修智库项目\XML源文件\HS7-RM源文件\topic\8AT变速箱'):
    for filename in filenames:
        if filename == "描述.dita":
            path = os.path.join(filepath,filename)
            plist.append(path)
# print(plist)

#print(plist[0])
#遍历list，打开文件，将文件内容
for i in plist:
    #打开XML文档
   DOMTree = xml.dom.minidom.parse(i)
    #得到文档对象
   topic = DOMTree.documentElement

   if topic.hasAttribute("id"):
       print("Root element : %s" % topic.getAttribute("id"))

   # 在集合中获取所有entry
   entrys = topic.getElementsByTagName("entry")

   s=0
    # 打印每个entry的详细信息
   for entry in entrys[3:]:

        if s==0:
            print("name : %s" % entry.childNodes[0].data)
            s+=1
            continue
            #print("DTC: %s" % entry.childNodes[1].data)
        #elif entry.hasAttribute("align")&entry.hasAttribute("valign")&s==1:
        elif s==1:
            print("检测条件 : %s" % entry.childNodes[0].data)
            s+=1
            #print(s)
            continue
        #elif entry.hasAttribute("valign") & (s==2):
        elif s==2:
            #正则表达式
            #pattern = re.compile('ab.+ef')  # 匹配从ab开始，到ef结束的内容
            # pattern = re.compile('<li>.+</li>')
            # result = pattern.findall(str)
            # print(result)

            # ul=entry.childNodes
            # #print(len(ul))
            # li=entry.getElementsByTagName("li")
            s=0
           # li1=ul.getElementsByTagName("li")
            #li=ul.childNodes[0].data
            #print(li)
            #s=0

        #print(s==2)
        #print(entry.hasAttribute("valign"))

#春上
# nodelists = data.getElementsByTagName("li")
#     print(nodelists[1].firstChild.data, end=' ')