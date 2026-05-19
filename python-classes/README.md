#  Classes and Objects in Python

##  Introduction

Object-Oriented Programming (OOP) is a programming paradigm that allows code to be organized using **classes** and **objects**.
In Python, this approach helps make programs more structured, reusable, and easier to maintain.

A **class** works like a blueprint, while an **object** is an actual instance created from that blueprint.

---

##  What Is a Class?

A **class** defines the attributes (data) and methods (actions) that objects created from it will have.

### Example:

```python
class Person:
    """Represents a person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)
```

### Key Points:

* `class Person:` defines a class.
* `__init__` is a constructor that initializes object data.
* `self` refers to the current object instance.
* Attributes: `name`, `age`.
* Method: `greet()`.

---

##  What Is an Object?

An **object** is an instance of a class.
It contains real values based on the class definition.

### Example:

```python
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

p1.greet()
p2.greet()
```

Output:

```
Hello, my name is Alice
Hello, my name is Bob
```

---

##  Attributes and Methods

### Attributes

Attributes store data inside an object.

Example:

```python
self.name = name
```

### Methods

Methods define actions an object can perform.

Example:

```python
def greet(self):
    print("Hello")
```

---

##  Private Attributes

In Python, attributes prefixed with double underscores (`__`) are treated as private.

Example:

```python
class Square:
    def __init__(self, size):
        self.__size = size
```

This helps protect internal data from direct modification.

---

##  Properties (Getter and Setter)

Properties allow controlled access to private attributes.

Example:

```python
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```

Benefits:

* Data validation
* Encapsulation
* Cleaner code

---

##  Example Project: Square Class

```python
class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2
```

Usage:

```python
sq = Square(4)
print(sq.area())  # Output: 16
```

---

##  Advantages of OOP

* Better code organization
* Reusability
* Easier maintenance
* Improved readability
* Scalability for large projects

---

##  Author

Eloy A. Alicea Sanchez
