# --------- Real-life Example 1: Student/Teacher System ---------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I am {self.name}, and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

s = Student("Aman", 20, "S123")
t = Teacher("Mrs. Sharma", 40, "Mathematics")
s.introduce()
s.study()
t.introduce()
t.teach()


# --------- Real-life Example 2: Employee Management ---------
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}")

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def manage(self):
        print(f"{self.name} is managing {self.department} department.")

e1 = Employee(101, "Ravi", 40000)
m1 = Manager(102, "Priya", 70000, "IT")
e1.display()
m1.display()
m1.manage()


# --------- Real-life Example 3: Library/Book System ---------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"📚 '{self.title}' by {self.author}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to library.")

    def show_books(self):
        print("Books in library:")
        for book in self.books:
            book.display()

book1 = Book("Python Basics", "John Doe")
book2 = Book("Data Structures", "Jane Smith")
lib = Library()
lib.add_book(book1)
lib.add_book(book2)
lib.show_books()
