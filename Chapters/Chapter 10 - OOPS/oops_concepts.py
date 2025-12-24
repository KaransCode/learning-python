# oops_concepts.py

# --------- 1. Class and Object ---------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"🚗 Car Brand: {self.brand}, Model: {self.model}")

# Creating Object
car1 = Car("Toyota", "Fortuner")
car1.show_details()


# --------- 2. Inheritance ---------
class ElectricCar(Car):  # Inheriting from Car
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def show_battery(self):
        print(f"🔋 Battery Capacity: {self.battery_capacity} kWh")

e_car = ElectricCar("Tesla", "Model S", 100)
e_car.show_details()
e_car.show_battery()


# --------- 3. Encapsulation ---------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(f"💰 Account Balance: ₹{account.get_balance()}")
# print(account.__balance)  # ❌ This will raise error (private variable)


# --------- 4. Abstraction ---------
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(f"🟢 Area of Circle: {circle.area()}")

# --------- 5. Polymorphism ---------
class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("🐶 Dog barks.")

class Cat(Animal):
    def speak(self):
        print("🐱 Cat meows.")

# Polymorphism in action
animals = [Dog(), Cat()]
for a in animals:
    a.speak()
