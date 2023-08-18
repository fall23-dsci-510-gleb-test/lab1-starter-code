import sys
import math

# For your reference
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5 / 9
    return temp_c

# For your reference
def circle_circumference(radius):
    return 2 * math.pi * radius

# Q1
def celsius_to_fahrenheit(temp_c):
    pass 

# Q2
def circle_area(radius):
    pass

# Q3
def cylinder_volume_surface(radius, height):
    pass

if __name__ == '__main__':

    fn_name = sys.argv[1]
    exp_out = sys.argv[-1]

    match fn_name:
        case 'circle_area':
            print(circle_area(float(sys.argv[2])))
        
        case 'celsius_to_fahrenheit':
            assert celsius_to_fahrenheit(float(sys.argv[2])) == float(exp_out)
        
        case 'cylinder_volume_surface':
            assert cylinder_volume_surface(float(sys.argv[2]), float(sys.argv[3])) == float(exp_out)


    

