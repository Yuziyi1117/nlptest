#one-hot 编码 操作简单容易理解，完全割裂了词语之间的联系，在大语料集之下向量长度过大，占据了大量内存

#导入用于对象保存和加载的包
import joblib
#导入keras
from keras_preprocessing.text import Tokenizer

#初始化一个词汇表,集合的形式
vocab  = {"周杰伦","李宗盛","林俊杰","王力宏","吴亦凡"}

#实例化一个词汇映射器
t = Tokenizer(num_words=None,char_level = False)

#在映射器上拟合现有的词汇表
t.fit_on_texts(vocab)

#循环遍历词汇表，将每一个单词映射为one-hot张量表示
for token in vocab:
    zero_list = [0] * len(vocab)
    #使用映射器转化文本数据，每个词汇对应从1开始
    token_index = t.texts_to_sequences([token])[0][0] - 1
    #将对应的位置赋值为1
    zero_list[token_index] = 1
    print(token,"的one-hot编码为：",zero_list)

#将拟合好的词汇映射器保存起来
tokenizer_path = "./Tokenizer"
joblib.dump(t,tokenizer_path) # Joblib是一组用于在Python中提供轻量级流水线的工具。特点：·透明的磁盘缓存功能和懒惰的重新评估（memoize模式）\·简单的并行计算.Joblib可以将模型保存到磁盘并可在必要时重新运行



t = joblib.load("./Tokenizer")

token = "李宗盛"
#从词汇映射器中得到该词语的index
token_index = t.texts_to_sequences([token])[0][0] - 1
#初始化一个全零向量
zero_list = [0] * len(vocab)
zero_list[token_index] = 1
print(token,"的one-hot编码为：",zero_list)