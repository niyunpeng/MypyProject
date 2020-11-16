#9.11
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("E:\\数字化部\\算法中心\\维修智库项目\\XML源文件\\E-HS3-RM源文件\\topic\\AC\\B130015 - B130007\\描述.dita")
topic = DOMTree.documentElement

temp = []
tempnode = topic.getElementsByTagName("tbody")
tempnode1 = tempnode[0].getElementsByTagName("row")
for templist in tempnode1:
    tempdict = {}
    tempdict['DTC 编号'] = templist[0].getElementsByTagName('row')[0]
    # tempdict['DTC 检测条件'] = templist.getElementsByTagName("row")[1]
    # for i in range(10):
    #     if templist.getElementsByTagName("row")[2].childNodes[i] !=None:
    #         tempdict['故障部位'] = templist.getElementsByTagName("row")[2].childNodes[i]
print(tempdict)

# if topic.hasAttribute("id"):
#     print("Root element : %s" % topic.getAttribute("id"))

# # 在集合中获取所有entry
# entrys = topic.getElementsByTagName("entry")
# tbody = topic.getiterator('tbody')
# print(tbody)
# #在集合中获取所有row
# entrys = topic.getElementsByTagName("entry")
#



# # 打印每个entry的详细信息
# for entry in entrys:
#     # print("*****row*****")
#     if entry.hasAttribute("id"):
#         # print("DTC: %s" % entry.getAttribute("title"))
#         print("DTC编号: %s" % entry.childNodes[0].data)
#     elif entry.hasAttribute("valign"):
#         print("DTC检测条件: %s" % entry.childNodes[0])
