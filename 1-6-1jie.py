#coding:utf-8

import jieba
content = ["机器学习带动发展"]  #这样是一个只有一个元素的列表，不是一个字符串。不带中括号才是字符串，才能直接cut

#
for i in range(len(content)):
#     for j in jieba.cut(content[i]):
#         print(j)
#    word_list= [word for word in jieba.cut(content[i])]
    word_list = list(jieba.cut(content[i]))
    print(word_list)
#jieba.cut返回一个生成器，利用一个for循环列表推导式或者list函数，将生成器对象赋给word_list列表，word_list即相当于jieba.lcut的返回

