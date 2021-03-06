#coding:utf-8

from gensim.models import Word2Vec
import jieba

# 定义停用词、标点符号
punctuation = ["，", "。", ":", ";", ".", "'", '”', "’", "?", "/", "-", "+", "&", "（", "）"]  #符号改成中文符号
sentences = [
    "长江是中国第一大河，干流全长6397公里（以沱沱河为源），一般称6300公里。流域总面积一百八十余万平方公里，年平均入海水量约九千六百余亿立方米。以干流长度和入海水量论，长江均居世界第三位。",
    "黄河，中国古代也称河，发源于中华人民共和国青海省巴颜喀拉山脉，流经青海、四川、甘肃、宁夏、内蒙古、陕西、山西、河南、山东9个省区，最后于山东省东营垦利县注入渤海。干流河道全长5464千米，仅次于长江，为中国第二长河。黄河还是世界第五长河。",
    "黄河,是中华民族的母亲河。作为中华文明的发祥地,维系炎黄子孙的血脉.是中华民族民族精神与民族情感的象征。",
    "黄河被称为中华文明的母亲河。公元前2000多年华夏族在黄河领域的中原地区形成、繁衍。",
    "在兰州的“黄河第一桥”内蒙古托克托县河口镇以上的黄河河段为黄河上游。",
    "黄河上游根据河道特性的不同，又可分为河源段、峡谷段和冲积平原三部分。 ",
    "黄河,是中华民族的母亲河。"
]

sentences = [j for i in range(len(sentences)) for j in jieba.cut(sentences[i]) ]  #第一个for是外循环，第二个是内循环
print(sentences)
tokenized = []

# for sentence in sentences:
#     words = []
#     for word in sentence:
#         if word not in punctuation:
#            words.append(word)
#     tokenized.append(words)
#print(words)
tokenized.append(sentences)
print(tokenized)

model = Word2Vec(tokenized, sg=1, size=100, window=5, min_count=2, negative=1, sample=0.001, hs=1, workers=4)

model.save('model')  # 保存模型
model = Word2Vec.load('model')  # 加载模型

print(model.similarity('长江', '黄河'))

print(model.most_similar(positive=['黄河', '母亲河'], negative=['长江']))

