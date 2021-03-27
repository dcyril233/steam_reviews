import jieba
import sys
import re


class Preprocess:
    
    # create object storing feature
    def __init__(self, raw_data, stop_words_path, pattern, userdict=None):
        self.stop_words = self.get_stop_words(stop_words_path)
        filter_p = re.compile(pattern)
        if(userdict != None):
            jieba.load_userdict(userdict)
        self.token = self.tokenization(raw_data, filter_p)


    def get_stop_words(self, path):
        stop_words = set()
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        	for line in f:
        		stop_words.add(line.strip('\n'))
        return stop_words

    def tokenization(self, data, filter_p):
        token = []
        length = len(data)
        for i in range(length):
            one_commt = data[i] # 取第i行
            one_commt = re.sub(filter_p, "", one_commt) # 去掉所有特殊字符
            seg_list = jieba.cut(one_commt, cut_all=True)
            comment = []
            for word in seg_list:
                if word not in self.stop_words:
                    comment.append(word)
            token.append(" ".join(comment))
        return token
            