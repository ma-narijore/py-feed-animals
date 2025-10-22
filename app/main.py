class Animal:
    def __init__(self, name: str, appetite: int, is_hungry: bool = True) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            return_number = self.appetite
            self.appetite -= self.appetite
            self.is_hungry = False
            return return_number
        else:
            return 0


class Cat(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite = 3, is_hungry=is_hungry)

    def catch_mouse(self) -> None:
        print("The hunt began!")

class Dog(Animal):
    def __init__(self, name: str, is_hungry: bool = True) -> None:
        super().__init__(name=name, appetite=7, is_hungry=is_hungry)

    def bring_slippers(self):
        print("The slippers delivered!")


if __name__ == "__main__":
    dog = Dog("Dog")
    dog.print_name()  # "Hello, I'm Dog"
    dog.feed()  # "Eating 7 food points"

    dog2 = Dog("Dog", False)
    print(dog2.feed())  # 0
    dog2.bring_slippers()