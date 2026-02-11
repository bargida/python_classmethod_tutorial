# class Polygon:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
# class Rectangle(Polygon):
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#     def area(self):
#         return self.length * self.width
# class Square(Polygon):
#     def __init__(self, side):
#         self.side=side
#     def perimeter(self):
#         return 4 * self.side
#     def area(self):
#         return self.side * self.side

# res = Rectangle(2, 5)
# print(res.perimeter())
# print(res.area())
# res1 = Square(4)
# print(res1.perimeter())
# print(res1.area())
    
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#     def area(self):
#         return self.length * self.width

# res = Polygon(2, 5)
# print(res.perimeter())
# print(res.area())
class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        super().move()
        print('Car is driving')
class Bicycle(Vehicle):
    def move(self):
        super().move()
        print('Bicycle is pedaling')
res = Car()
res.move()
res1 = Bicycle()
res1.move()




