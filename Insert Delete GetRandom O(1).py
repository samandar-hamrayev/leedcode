import random


class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.lst.append(val)
        self.mp[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        index = self.mp[val]
        self.lst[index] = self.lst[-1]
        self.mp[self.lst[-1]] = index
        self.lst.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)