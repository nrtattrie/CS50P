

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Can't have negative capacity")
        else:
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        cookies = ""
        n = 0
        while n < self.size:
            cookies = cookies + "🍪"
            n += 1
        return cookies

    def deposit(self, n):
        if (self.size + n) <= self.capacity:
            self.size = self.size + n
        else:
            raise ValueError()

    def withdraw(self, n):
        if (self.size - n) >= 0:
            self.size = self.size - n
        else:
            raise ValueError()

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)



if __name__ == "__main__":
    main()

