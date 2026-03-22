class Apple:
    states = {0: "Відсутнє", 1: "Цвітіння", 2: "Зелене", 3: "Червоне"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class AppleTree:
    def __init__(self, count):
        self.apples = [Apple(i) for i in range(count)]

    def grow_all(self):
        for apple in self.apples:
            apple.grow()

    def all_are_ripe(self):
        return all(apple.is_ripe() for apple in self.apples)

    def give_away_all(self):
        self.apples = []


class Gardener:
    def __init__(self, name, tree):
        self.name = name
        self._tree = tree

    def work(self):
        print(f"Садівник {self.name} працює...")
        self._tree.grow_all()

    def harvest(self):
        if self._tree.all_are_ripe():
            print("Збір врожаю...")
            self._tree.give_away_all()
            print("Врожай зібрано!")
        else:
            print("Яблука ще не дозріли.")

    @staticmethod
    def apple_base(apples):
        print("Довідка по яблуках:")
        for apple in apples:
            print(f"  Яблуко #{apple._index}: стадія - {Apple.states[apple._state]}")


if __name__ == '__main__':
    print("--- Тести Завдання 3 ---")
    
    apple1 = Apple(0)
    apple2 = Apple(1)
    apple3 = Apple(2)
    Gardener.apple_base([apple1, apple2, apple3])
    
    tree = AppleTree(3)
    gardener = Gardener("Петро", tree)
    
    gardener.work()
    gardener.harvest()
    
    gardener.work()
    gardener.work()
    
    print(f"Чи всі яблука дозріли? {tree.all_are_ripe()}")
    gardener.harvest()
    print(f"Яблук на дереві: {len(tree.apples)}")
