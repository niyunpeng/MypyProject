
from transformers import BertTokenizer,BertModel
import torch
import pandas as pd


tokenizer = BertTokenizer.from_pretrained(r'E:\数字化部\算法中心\维修智库项目\痛点2_故障描述中存在大量同义描述\bert\chinese-bert_chinese_wwm_pytorch/data')
model = BertModel.from_pretrained(r'E:\数字化部\算法中心\维修智库项目\痛点2_故障描述中存在大量同义描述\bert\chinese-bert_chinese_wwm_pytorch/data')
#f=pd.ExcelFile(r'C:\Users\sunyue18\Desktop\华为数据\痛点2\FAW_excel_数据汇总.xlsx')
f=pd.ExcelFile(r'E:\数字化部\算法中心\维修智库项目\痛点2_故障描述中存在大量同义描述\FAW_excel_数据汇总 - 副本.xlsx')
sheet1 = pd.read_excel(f,'质量反馈单跟踪')
descs = sheet1[['故障描述']].values

temp = 0
temp1 = 0
for i in descs:
    i = str(i)
    input_ids = torch.tensor([tokenizer.encode(str(descs[100]),add_special_tokens=False)])  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    # print(input_ids)
    with torch.no_grad():
        last_hidden_states = model(input_ids)[0]  # Models outputs are now tuples
        #print(last_hidden_states)
    # input_ids = torch.tensor([tokenizer.encode(i,add_special_tokens=False)])  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    input_ids = torch.tensor([tokenizer.encode(i,add_special_tokens=False)])  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.
    # input_ids = torch.tensor([tokenizer.encode("下雨天开雨刮车身发抖",add_special_tokens=False)])  # Add special tokens takes care of adding [CLS], [SEP], <s>... tokens in the right way for each model.

    with torch.no_grad():
        last_hidden_states2 = model(input_ids)[0]  # Models outputs are now tuples
        #print(last_hidden_states2)

    from sklearn.metrics.pairwise import  cosine_similarity
    last_hidden_states = torch.mean(last_hidden_states,dim=1)
    last_hidden_states2 = torch.mean(last_hidden_states2,dim=1)
    cos = cosine_similarity(last_hidden_states,last_hidden_states2)

    if cos > temp:
        temp = cos
        temp1 = i
    #print("cos_simi:",cos)
        print('相似度：',temp,'描述语句：',temp1)
