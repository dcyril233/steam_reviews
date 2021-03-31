import re
import jieba


class Filter:
    def invoke(self, data):
        pass


class ReFilter(Filter):
    def __init__(self, pattern):
        self.filter_p = re.compile(pattern)

    def invoke(self, data):
        return re.sub(self.filter_p, "", data)  # 去掉所有特殊字符


class CommentFilter(Filter):
    def __init__(self, userdict):
        if (userdict != None):
            jieba.load_userdict(userdict)

    def invoke(self, data):
        return jieba.cut(data, cut_all=True)


class TokenFilter(Filter):
    def __init__(self, stop_words_path):
        self.stop_words = self.get_stop_words(stop_words_path)

    @staticmethod
    def get_stop_words(path):
        stop_words = set()
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                stop_words.add(line.strip('\n'))
        return stop_words

    def invoke(self, data):
        comment = []
        for word in data:
            if word not in self.stop_words:
                comment.append(word)
        return comment
