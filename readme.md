# Python Class Methods Tutorial

## Table of Contents
1. [Introduction to Decorators](#introduction-to-decorators)
2. [Factory Design Patterns using @classmethod](#factory-design-patterns-using-classmethod)

## Introduction to Decorators

Decorators in Python are a powerful way to modify the behavior of functions or classes. They wrap another function to extend its behavior without explicitly modifying it.

In the context of methods, decorators like `@classmethod` and `@staticmethod` alter how a method is called and what arguments it receives.

- **`@classmethod`**: This decorator transforms a method into a class method. Instead of receiving the instance (`self`) as the first argument, it receives the class (`cls`).

```python
class MyClass:
    @classmethod
    def my_class_method(cls):
        print(f"Called on {cls}")
```

## Factory Design Patterns using @classmethod

A common use case for `@classmethod` is to implement the Factory Pattern. This allows a class to have multiple ways to create an instance, acting as alternative constructors.

For example, creating an instance from a date string vs. separate year/month/day arguments:

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

# Standard constructor
d1 = Date(2023, 10, 27)

# Factory method
d2 = Date.from_string('2023-10-27')
```
