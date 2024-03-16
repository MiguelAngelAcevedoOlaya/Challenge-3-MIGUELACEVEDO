import math

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.compute_length()
        self.compute_slope()
    
    def compute_length(self) -> float:
        self.length = (( ((self.end[0]- self.start[0])**2) + ((self.end[1]- self.start[1])**2)  )**(0.5))
        
    def compute_slope(self) -> float:
        delta_y = self.end[1] - self.start[1]
        delta_x = (self.end[0] - self.start[0])
        self.slope = math.atan2(delta_y, delta_x)
        self.slope = math.degrees(self.slope)
    
    def compute_horizontal_cross(self):
        if self.start[0] <= 0:
            if self.end[0] <= 0:
                return False
            else: return True

        elif self.end[0] <= 0:
            if self.start[0] <= 0:
                return False
            else: return True
            
        else: return False
    
    def compute_vertical_cross(self):
        if self.start[1] <= 0:
            if self.end[1] <= 0:
                return False
            else: return True

        elif self.end[1] <= 0:
            if self.start[1] <= 0:
                return False
            else: return True
            
        else: return False
    
if __name__ == "__main__":
    linea= Line(start= ((int(input("Enter the x1 ")), int(input("Enter the y1: ")))), end=((int(input("Enter the x2: ")), int(input("Enter the y2: ")))))
    print("Length:", linea.length)
    print("Slope:", linea.slope, "°")
    print("Horizontal Intersection:", linea.compute_horizontal_cross())
    print("Vertical Intersection:", linea.compute_vertical_cross())