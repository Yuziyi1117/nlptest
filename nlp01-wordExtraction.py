#coding:utf-8

import jieba.analyse

sentence = "人工智能（Artificial Intelligence），英文缩写为AI。它是研究、开发用于模拟、延伸和扩展人的智能的理论、方法、技术及应用系统的一门新的技术科学。人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器，该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大，可以设想，未来人工智能带来的科技产品，将会是人类智慧的“容器”。人工智能可以对人的意识、思维的信息过程的模拟。人工智能不是人的智能，但能像人那样思考、也可能超过人的智能。人工智能是一门极富挑战性的科学，从事这项工作的人必须懂得计算机知识，心理学和哲学。人工智能是包括十分广泛的科学，它由不同的领域组成，如机器学习，计算机视觉等等，总的说来，人工智能研究的一个主要目标是使机器能够胜任一些通常需要人类智能才能完成的复杂工作。但不同的时代、不同的人对这种“复杂工作”的理解是不同的。2017年12月，人工智能入选“2017年度中国媒体十大流行语”。"
keywords = "  ".join(jieba.analyse.extract_tags(sentence, topK=20, withWeight=False))
#print(keywords)
result = "  ".join(jieba.analyse.textrank(sentence, topK=20, withWeight=False,))  #allowPOS=('ns', 'n', 'vn', 'v') 该版本没有allowPOS这个参数了
print(result)

#conda+3.7环境，所以使用的实际是jieba3k。jieba3k没有贡献lcut这个方法，我现在改用cut得到迭代器之后用word直接调用了。