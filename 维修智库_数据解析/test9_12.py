import time
import re
import os
import os.path
import xml.dom.minidom
import re
from xml.dom.minidom import parse

from bs4 import BeautifulSoup
import requests

plist=[]
for filepath,dirnames,filenames in os.walk(r'E:\数字化部\算法中心\维修智库项目\XML源文件\HS7-RM源文件\topic\8AT变速箱'):
    for filename in filenames:
        if filename == "描述.dita":
            path = os.path.join(filepath,filename)
            plist.append(path)
# print(plist)

###遍历list，打开文件，将文件内容
for i in plist:
    ###打开XML文档
    DOMTree = xml.dom.minidom.parse(i)
    ###得到文档对象
    topic = DOMTree.documentElement
    # print(topic)

    ### 在集合中获取所有entry
    entrys = topic.getElementsByTagName("entry")
    # print(entrys)

    # for entry in entrys[3:]:
        #print(entry.children[0])#?
    nodelists = entry.getElementsByTagName("li")
    print(nodelists[1].firstChild.data, end=' ')