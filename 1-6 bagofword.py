#coding:utf-8

import jieba
#定义停用词、标点符号
punctuation = ["，","。", "：", "；", "？"]
#定义语料
content = ["机器学习带动人工智能飞速的发展。",
               "深度学习带动人工智能飞速的发展。",
               "机器学习和深度学习带动人工智能飞速的发展。"
              ]
#
#for i in segs_1:
# # 分词
#print(i)
for i in range(len(content)):
#     for j in jieba.cut(content[i]):
#         print(j)
# for i in range(len(content)):
#     print('/'.join(jieba.cut(content[i])))
# segs_1 = [j for j in jieba.cut(content(j))]
    segs_1 = [wr for wr in jieba.cut(content[i])]
    print(segs_1)
    tokenized = []
    words = []
    for word in segs_1:
        if word not in punctuation:
            words.append(word)
    tokenized.append(words)
    print(tokenized)

# 求并集
bag_of_words = [x for item in segs_1 for x in item if x not in punctuation]
# 去重
bag_of_words = list(set(bag_of_words))
print(bag_of_words)

bag_of_word2vec = []
for sentence in tokenized:
    tokens = [1 if token in sentence else 0 for token in bag_of_words]
    bag_of_word2vec.append(tokens)






