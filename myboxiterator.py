class MyBoxIterator:
    def __init__(self, l):
        self.l = l
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind < len(self.l):
            item = self.l[self.ind]
            self.ind += 1
            return item
        else:
            raise StopIteration

