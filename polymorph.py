class Shape:
    def area(self):
        print("describes the area of derived shape obj")


class Circle(Shape):
    def area(self):
        radius=float(input("enter radius: "))
        result= 3.14*radius*radius
        print("for radius", radius)
        print("area of circle is", result)

obj=Shape()
obj.area()
print(id(obj))
obj2=obj
print(id(obj))
obj=Circle()
obj.area()
print(id(obj))