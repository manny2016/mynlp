#coding=utf-8
import os as os
import json as json
import io as io
from pprint import pprint
import codecs as codecs
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.models import Word2Vec
import sys as sys
import logging 
"""
MSDN 论坛帖子分类基本思路:
1.使用 Word2vec 提取词向量，建立语料库。数据采用当前 SHP系统做已分词结束的所有post 以及reply
2.使用CBOW模型通过上下文预定给定的词.
3.再使用 Skip_gram 来 进行分类

Word2vec 参数详解
· sentences：可以是一个·ist，对于大语料集，建议使用BrownCorpus,Text8Corpus或·ineSentence构建。
·  sg： 用于设置训练算法，默认为0，对应CBOW算法；sg=1则采用skip-gram算法。
·  size：是指特征向量的维度，默认为100。大的size需要更多的训练数据,但是效果会更好. 推荐值为几十到几百。
·  window：表示当前词与预测词在一个句子中的最大距离是多少
·  alpha: 是学习速率
·  seed：用于随机数发生器。与初始化词向量有关。
·  min_count: 可以对字典做截断. 词频少于min_count次数的单词会被丢弃掉, 默认值为5
·  max_vocab_size: 设置词向量构建期间的RAM限制。如果所有独立单词个数超过这个，则就消除掉其中最不频繁的一个。每一千万个单词需要大约1GB的RAM。设置成None则没有限制。
·  sample: 高频词汇的随机降采样的配置阈值，默认为1e-3，范围是(0,1e-5)
·  workers参数控制训练的并行数。
·  hs: 如果为1则会采用hierarchica·softmax技巧。如果设置为0（defau·t），则negative sampling会被使用。
·  negative: 如果>0,则会采用negativesamp·ing，用于设置多少个noise words
·  cbow_mean: 如果为0，则采用上下文词向量的和，如果为1（defau·t）则采用均值。只有使用CBOW的时候才起作用。
·  hashfxn： hash函数来初始化权重。默认使用python的hash函数
·  iter： 迭代次数，默认为5
·  trim_rule： 用于设置词汇表的整理规则，指定那些单词要留下，哪些要被删除。可以设置为None（min_count会被使用）或者一个接受()并返回RU·E_DISCARD,uti·s.RU·E_KEEP或者uti·s.RU·E_DEFAU·T的函数。
·  sorted_vocab： 如果为1（defau·t），则在分配word index 的时候会先对单词基于频率降序排序。
·  batch_words：每一批的传递给线程的单词的数量，默认为10000

"""


#Initialize and train a Word2Vec model
#sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]
#model = Word2Vec(sentences, min_count = 1)
def ready_vocabularies():
    """
    遍历JSON文件获取所有的 sentences
    """
    vocabulary = []
    path = "D:\context\MSDN"        
    for name in os.listdir(path):        
        #if name.endswith("17179.txt") == False:
        #    continue
        fullName = os.path.join(path,name)
        pprint(fullName)
        with open(fullName,'r',encoding="utf8",errors="errors") as myjson:
            text = myjson.read()            
            if(text.startswith(u'\ufeff')):
                text = text.encode('utf8')[3:].decode('utf8')
            #python 内部使用 unicode 因此对于任何非 unicode的编码在输出时候都需要将其转换为原来的编码
            #也就是说不管什么格式的当
            #python read 以后都会变成 unicode , 在重新输出时候需要encode为原来的编码
            #否则会报错（在print时候需要这样做)
            #http://blog.sina.com.cn/s/blog_63f0cfb20100jim1.html
            json_data = json.loads(text)            
            for sentence in json_data:
                for word in sentence["Value"]:
                    if word is None:
                        continue
                    try:
                        words = []
                        #pprint(word.encode('utf8').decode('utf8'))
                        words.append(word.encode('utf8').decode('utf8'))
                        vocabulary.append(words) #以句子为单位导入词库
                    except UnicodeEncodeError:
                        #忽略某些非英文的单词例如俄语，以及 “等不能转换编码的字符
                        continue
                    except AttributeError:
                        #None NoneType 等于其他语言的 null
                        #忽略 None
                        continue
                    finally:
                        del words
               
    del sentence        
    return vocabulary

def training(sentences):
    model = Word2Vec(sentences,min_count=1,size=200,sg=0)
    model.save("msdn.model")
    
library = ready_vocabularies()
training(library)








