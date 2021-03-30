
class Calculator:
    def __init__(self):
        self.add(10, 20)
        self.subtract(10, 20)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


if __name__ == '__main__':
    calculator = Calculator()
