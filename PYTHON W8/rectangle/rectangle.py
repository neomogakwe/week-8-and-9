 
import calculate

length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle: "))

area = calculate.area(length, breadth)
perimeter = calculate.perimeter(length, breadth)

print(f"The area of the rectangle is: {area}")
print(f"The perimeter of the rectangle is: {perimeter}")