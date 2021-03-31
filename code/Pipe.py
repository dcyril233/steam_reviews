from Filter import ReFilter, CommentFilter, TokenFilter


class Pipe:
    def __init__(self, stop_words_path, pattern, userdict=None):
        self.filters = []
        self.filters.append(ReFilter(pattern))
        self.filters.append(CommentFilter(userdict))
        self.filters.append(TokenFilter(stop_words_path))

    def invoke(self, raw_data):
        token = []
        length = len(raw_data)
        for i in range(length):
            data = raw_data[i]
            for f in self.filters:
                data = f.invoke(data)
            token.append(" ".join(data))
        return token
