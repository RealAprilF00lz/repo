class Jar:
    def __init__(self, capacity=12):
        if type(capacity)!=int or capacity<0:
            raise ValueError
        self._capacity=capacity 
        self.cookies=0

    def __str__(self):
        x=''
        for i in range(self.cookies):
            x+='🍪'
        return x

    def deposit(self, n):
        if self.cookies+n>self._capacity:
            raise ValueError
        self.cookies+=n

    def withdraw(self, n):
        if self.cookies<n:
            raise ValueError
        self.cookies-=n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
