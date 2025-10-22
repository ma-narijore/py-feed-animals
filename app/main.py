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


if __name__ == "__main__":
    cat = Cat("Cat")
    cat.print_name()  # "Hello, I'm Cat"
    cat.feed()  # "Eating 3 food points"

    cat2 = Cat("Cat", False)
    print(cat2.feed())  # 0
    cat2.catch_mouse()