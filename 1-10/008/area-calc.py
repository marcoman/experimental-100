import math

def calc_area(length, width):
    return length * width

def calc_area_with_coverage(length, width, coverage):
    return (length * width) / coverage

height = float(input("Enter height: "))
width = float(input("Enter width: "))
coverage = float(input("Enter coverage: "))
area = calc_area(height, width)
print("Area:", area)

coverage =  calc_area_with_coverage(height, width, coverage)
print (f'Your area of {area} needs {math.ceil(coverage)} cans')