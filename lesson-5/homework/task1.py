from math import*

def convert_cel_to_far(c):
    return c*9/5+32
def convert_far_to_cel(f):
    return (f-32)*5/9

far=float(input("Enter a temperature in degrees F: "))
print(far, "degrees F =", round(convert_far_to_cel(far),2), "degrees C")

cel=float(input("Enter a temperature in degrees C: "))
print(cel, "degrees C =", round(convert_cel_to_far(cel),2), "degrees F")