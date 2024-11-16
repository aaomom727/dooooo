class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.energy = 100

    def sound(self):
        print(f"{self.name} говорит: Гав-гав!")

    def eat(self):
        self.energy += 20
        print(f"{self.name} ест. Энергия: {self.energy}")

    def walk(self):
        print(f"{self.name} гуляет")


dog = Dog("Фидо", 3)

dog.sound()
dog.eat()
dog.walk()
