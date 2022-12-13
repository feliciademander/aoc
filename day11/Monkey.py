# Monkey


class Monkey:
    def __init__(self, id: int, startItems: list, divisor: int, operation, nextIfTrue: int, nextIfFalse: int):
        self.id = id
        self.items = startItems
        self.divisor = divisor
        self.operation = operation
        self.nextIfTrue = nextIfTrue
        self.nextIfFalse = nextIfFalse
        self.current = -1
        self.inspections = 0

    def throwTo(self) -> int:
        divisible = self.current % self.divisor == 0
        # print(f'{self.current} % {self.divisor} == 0? {divisible}')
        if divisible:
            return self.nextIfTrue
        return self.nextIfFalse

    def turn(self) -> int:
        self.current = self.items.pop(0)
        self.inspections += 1
        # print(f'  Inspects a worry level of {self.current}')
        self.current = self.operation(self.current)
        self.current = self.current // 3
        # print(f'    Worry level is divided by 3 to {self.current}')
        return self.throwTo()

    def __str__(self): return f'Monkey {self.id}: {self.items}'
