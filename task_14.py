class EvenNumbers:
    def __init__(self, num):
        self.n = num
        self.even = []
        for i in range(self.n):
            self.even.append(2 * i)

    def __iter__(self):
        it = iter(self.even)
        return it


evens = EvenNumbers(5)
for num in evens:
    print(num)
