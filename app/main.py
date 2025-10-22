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

if __name__ == "__main__":
    lion = Animal("Lion", 25)
    lion.print_name()  # "Hello, I'm Lion"
    food_points = lion.feed()  # "Eating 25 food points..."
    print(food_points)  # 25
    print(lion.is_hungry)  # False
    print(lion.feed())  # 0