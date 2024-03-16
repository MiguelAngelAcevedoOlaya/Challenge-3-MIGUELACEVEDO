class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0

class Rectangle:
    definition: str = "A geometric form with 4 four sides, in the cartesiane plane"
    
    def __init__(self, method):
        if method == 1:
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x = bottom_left_corner_x , y = bottom_left_corner_y)
            
            width = int(input("Enter de widht: "))
            height = int(input("Enter the height: "))
            
            self.bottom_left_corner = bottom_left_corner
            self.blc_x = bottom_left_corner_x
            self.blc_y = bottom_left_corner_x
            self.width = width
            self.height = height
        
        elif method == 2:            
            center_point_x = int(input("Enter the x coordinate of the center : "))
            center_point_y = int(input("Enter the y coordinate of the center: "))
            center_point = Point(x = center_point_x , y = center_point_y)
            
            width = int(input("Enter de widht: "))
            height = int(input("Enter the height: "))
            
            self.center_point = center_point
            self.c_x = center_point_x
            self.c_y = center_point_y
            self.width = width
            self.height = height
        
        elif method == 3:
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x = bottom_left_corner_x , y = bottom_left_corner_y)
            
            upper_right_corner_x = int(input("Enter the x coordinate of the upper left corner: "))
            upper_right_corner_y = int(input("Enter the y coordinate of the upper left corner: "))
            upper_right_corner = Point(x = upper_right_corner_x , y = upper_right_corner_y)
            
            if bottom_left_corner_x >= upper_right_corner_x:
                return ("You didn´t put propperly the coordinates")
            elif bottom_left_corner_y >= upper_right_corner_y:
                return ("You didn´t put propperly the coordinates")
            
            
            width= upper_right_corner_x - bottom_left_corner_x
            height = upper_right_corner_y - bottom_left_corner_y
            
            self.bottom_left_corner = bottom_left_corner
            self.upper_right_corner = upper_right_corner
            self.blc_x = bottom_left_corner_x
            self.blc_y = bottom_left_corner_x
            self.upc_x = upper_right_corner_x
            self.upc_y = upper_right_corner_y
            self.width = width
            self.height = height
        
        else: 
            print("Men, please enter something valid, just 1 2 or 3")
            
    def compute_area(self):
        area= self.width * self.height
        return area
    
    def compute_perimeter(self):
        perimeter = 2*self.width + 2*self.height
        return perimeter
    
    def compute_interference_point(self, method, Point):
        if method == 1:
            if self.blc_x <= point.x <= self.blc_x + self.width and \
            self.blc_y <= point.y <= self.blc_y + self.height:
                return True
            else:
                return False
            
        elif method == 2:
            if self.center_point.x - (self.width/2) <= point.x <= self.center_point.x + (self.width/2) and \
            self.center_point.y - (self.height/2) <= point.y <= self.center_point.y + (self.height/2):
                return True
            else:
                return False


        elif method == 3:
            if self.blc_x <= point.x <= self.upc_x and \
            self.blc_y <= point.y <= self.upc_y:
                return True
            else:
                return False
    
        
class Square(Rectangle):
    definition: str = "A geometric form with 4 four equal sides, in the cartesian plane"

    def __init__(self, method):
        super().__init__(method)

        if self.width != self.height:
            print("A square must have equal width and height.")
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
        

method = int(input("Enter the method that you want (1, 2, or 3): "))
rectangle = Rectangle(method)

print("The area is", rectangle.compute_area())
print("The perimeter is", rectangle.compute_perimeter())

point = Point(x=int(input("Enter the x coordinate of the point: ")), y=int(input("Enter the y coordinate of the point: ")))
if rectangle.compute_interference_point(method, point):
    print("The point is in the rectangle")
else: 
    print("The point isn't in the rectangle")
    
print("\n")

print("Now we are gonna do with the square")
    
method = int(input("Enter the method that you want (1, 2, or 3) for Square: "))
cuadrado = Square(method)

print("The area is", cuadrado.compute_area())
print("The perimeter is", cuadrado.compute_perimeter())

point = Point(x=int(input("Enter the x coordinate of the point: ")), y=int(input("Enter the y coordinate of the point: ")))
if cuadrado.compute_interference_point(method, point):
    print("The point is in the square")
else: 
    print("The point isn't in the square")


