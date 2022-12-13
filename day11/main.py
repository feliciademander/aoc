# Day 11
from Monkey import Monkey
filename = "./input_2.txt"
MAX_ROUNDS = 20


def get_monkeys(monkey_strings: list) -> list:
    objects = []
    for s in monkey_strings:
        print("Monkey_string: '''" + s + "'''")
    return objects


def read_data() -> list:
    f = open(filename, "r")
    data = f.read()
    monkeys = data.split("\n\n")
    return get_monkeys(monkeys)


def print_inventories(monkeys: list) -> None:
    print("--------------------Inventories----------------------")
    for m in monkeys:
        print(m)
    print("-----------------------------------------------------\n")


def calc_monkey_business(monkeys: list) -> None:
    ins = []
    for m in monkeys:
        print(f'Monkey {m.id} inspected items {m.inspections} times.')
        ins.append(m.inspections)

    ins.sort(reverse=True)
    print(f'Two most active monkeys: {ins[0]} and {ins[1]}')
    print(f'Level of monkey business: {ins[0] * ins[1]}')


def start(monkeys: list):
    round = 0
    print_inventories(monkeys)

    while round < MAX_ROUNDS:
        round += 1
        # print(f'Round {round}!')

        for m in monkeys:
            # print(f'Monkey {m.id}:')
            while len(m.items) > 0:
                throwTo = m.turn()
                # print(f'    Throwing {m.current} to monkey {throwTo}')
                monkeys[throwTo].items.append(m.current)
                m.current = -1

        # print_inventories(monkeys)
    calc_monkey_business(monkeys)


if __name__ == "__main__":
    print("AOC Day 11")
    # monkeys = read_data()
    def a(x: int) -> int: return x * 2
    def b(x: int) -> int: return x * 13
    def c(x: int) -> int: return x + 5
    def d(x: int) -> int: return x + 6
    def e(x: int) -> int: return x + 1
    def f(x: int) -> int: return x + 4
    def g(x: int) -> int: return x + 2
    def h(x: int) -> int: return x * x
    monkeys = [
        Monkey(0, [98, 89, 52], 5, a, 6, 1),
        Monkey(1, [57, 95, 80, 92, 57, 78], 2, b, 2, 6),
        Monkey(2, [82, 74, 97, 75, 51, 92, 83], 19, c, 7, 5),
        Monkey(3, [97, 88, 51, 68, 76], 7, d, 0, 4),
        Monkey(4, [63], 17, e, 0, 1),
        Monkey(5, [94, 91, 51, 63], 13, f, 4, 3),
        Monkey(6, [61, 54, 94, 71, 74, 68, 98, 83], 3, g, 2, 7),
        Monkey(7, [90, 56], 11, h, 3, 5),
    ]
    start(monkeys)
