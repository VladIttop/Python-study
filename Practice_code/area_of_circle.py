#Area of circle equation is pi * r^2
import math

user_radius = float(input("Enter the radius of the circle: "))
area = math.pi * (user_radius ** 2)
print(f"The area of the circle with radius {user_radius} is: {area}")