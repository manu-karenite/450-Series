from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def printRadius(self):
        print(self.radius)

    def printArea(self):
        print("The area of Circle is : ", pi*self.radius**2)

    def printCircum(self):
        print("Circumference of Circle is : ", 2*pi*self.radius)


def main():
    # create an object
    r = float(input("Please enter the radius of Circle : "))
    obj = Circle(r)
    obj.printArea()
    obj.printCircum()


if __name__ == "__main__":
    main()
