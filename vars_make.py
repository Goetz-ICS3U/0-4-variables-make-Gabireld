#Gabriel Diab
#February 12th, 2026
#0.4-Variables-Make



#input

# get radius of circle
circ_radius = int(input("Please enter the radius of the circle: "))

# get length and width of the rectangle
rec_length = int(input("Please enter the length of the rectangle: "))
rec_width = int(input("Please enter the width of the rectangle: "))

# get side length of the octogram
octo_length = int(input("Please enter the side length of the octagon: "))



#processing

# import math
import math
p = math.pi
s = math.sqrt

#circumference of circle
circu = 2*p*circ_radius

#area of circle
circ_area = p*circ_radius**2

#perimeter of rectangle
rec_perm = (2*rec_length) + (2*rec_width)

#area of rectangle
rec_area = rec_length*rec_width

#perimeter of octagon
octo_perm = 8*octo_length

#area of octagon
octo_area = 2*(1+s(2))*octo_length**2



#Output

#space between input and output
print("")

#circumference of circle
print(f"The curcumference of the circle is: {circu}")

#area of circle
print(f"The area of the circle is: {circ_area}")

#perimeter of rectangle
print(f"The perimeter of the rectangle is: {rec_perm}")

#area of rectangle
print(f"The area of the rectangle is: {rec_area}")

#perimeter of octagon
print(f"The perimeter of the octagon is: {octo_perm}")

#area of octagon
print(f"The area of the octagon is: {octo_area}")