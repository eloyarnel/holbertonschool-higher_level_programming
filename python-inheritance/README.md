# Python - Inheritance

## Description

This project introduces **inheritance** in Python using Object-Oriented Programming (OOP).

Inheritance allows a class to reuse attributes and methods from another class, promoting:
- Code reusability
- Cleaner architecture
- Logical class hierarchy

The project builds a class structure starting from a base class and extending it into more specific shapes.

---

## Concepts Covered

- Inheritance (`class Child(Parent)`)
- Method overriding
- `super()`
- Private attributes (`__attribute`)
- Exception handling
- Type and value validation
- `type()` vs `isinstance()`

---

## Class Hierarchy

BaseGeometry
→ Rectangle
→ Square

Each subclass extends and specializes the behavior of its parent class.

---

## Features Implemented

- Abstract-like method `area()` raising an exception
- Integer validation using `integer_validator`
- Rectangle with width and height validation
- Square inheriting from Rectangle
- Custom string representations using `__str__`

---

## Example

```python
r = Rectangle(3, 5)
print(r)
print(r.area())

s = Square(4)
print(s)
print(s.area())

AUTHOR
Eloy A. Alicea Sanchez
