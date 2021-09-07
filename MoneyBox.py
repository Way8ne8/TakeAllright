class MoneyBox:
    def __init__(self, capacity):
        self.cap = capacity

    def can_add(self, v):
        if self.cap - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.cap -= v
            #print('Added', self.cap)
            return True
        else:
            #print('Error', self.cap)
            return False


x = MoneyBox(int(input()))
while True:
    v = int(input())
    x.add(v)


