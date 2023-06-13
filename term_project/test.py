class a:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def __str__(self):
        return str(self.a) + str(self.b) + str(self.c)

def b(ab):
    ab.a = 4

if __name__ == "__main__":
    a0 = a()
    print(a0.__str__())
    b(a0)
    print(a0.__str__())