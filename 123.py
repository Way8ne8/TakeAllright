class Buffer:

    def __init__(self):
        self.count = 0
        self.p = []

    def add(self, *a):
        #p = []
        for i in a:
            self.count+=1
            self.p.append(i)
        k = len(self.p)//5
        if k > 0:
            for q in range(k):
                s = 0
                for j in self.p[0:5]:
                    s+=j
                print(s)
                del self.p[0:5]

    def get_current_part(self):
        #print(self.p)
        return self.p
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
#p= []
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()  # вернуть [1, 2, 3]
buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part()  # вернуть [6]
buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part()  # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part()  # вернуть [1]