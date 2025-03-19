class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.lst = self._setter(nestedList)
        self.idx = 0

    def next(self) -> int:
        val = self.lst[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.lst)

    def _setter(self, lst):
        res = []
        for item in lst:
            if item.isInteger():
                res.append(item.getInteger())
            else:
                res.extend(self._setter(item.getList()))
        return res