a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

sides = sorted([a, b, c])

if sides[0] + sides[1] > sides[2]:

    if round(sides[0]**2 + sides[1]**2, 2) == round(sides[2]**2, 2):
        print("Right Angled Triangle")
    else:
        print("Not a Right Angled Triangle")

    s = (a + b + c) / 2

    area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

    print("Area of Triangle:", area)

else:
    print("Invalid Triangle")