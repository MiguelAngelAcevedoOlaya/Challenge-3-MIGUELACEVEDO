# Challenge 3 MIGUELACEVEDO

## RECTANGLE POINT

Este código crea clases en Python para manejar geometría en un plano cartesiano. La clase Point permite representar puntos en el plano, mientras que Rectangle y Square son para trabajar con rectángulos y cuadrados respectivamente. Puedes definir estos objetos con diferentes métodos (por ejemplo, especificando esquinas o centro y tamaño) y luego calcular áreas, perímetros, y verificar si un punto está dentro de ellos.

``` python
class Point:
    # Definition of the Point class
    definition: str = "Abstract geometric entity that represents a location in space."

    # Constructor method for the Point class
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    # Method to move the point to a new location
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y

    # Method to reset the point to the origin
    def reset(self):
        self.x = 0
        self.y = 0


class Rectangle:
    # Definition of the Rectangle class
    definition: str = "A geometric form with four sides, in the Cartesian plane."

    # Constructor method for the Rectangle class
    def __init__(self, method):
        # Method 1: Define rectangle by bottom-left corner and dimensions
        if method == 1:
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x=bottom_left_corner_x, y=bottom_left_corner_y)

            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))

            self.bottom_left_corner = bottom_left_corner
            self.blc_x = bottom_left_corner_x
            self.blc_y = bottom_left_corner_x
            self.width = width
            self.height = height

        # Method 2: Define rectangle by center point and dimensions
        elif method == 2:
            center_point_x = int(input("Enter the x coordinate of the center : "))
            center_point_y = int(input("Enter the y coordinate of the center: "))
            center_point = Point(x=center_point_x, y=center_point_y)

            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))

            self.center_point = center_point
            self.c_x = center_point_x
            self.c_y = center_point_y
            self.width = width
            self.height = height

        # Method 3: Define rectangle by bottom-left and upper-right corners
        elif method == 3:
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x=bottom_left_corner_x, y=bottom_left_corner_y)

            upper_right_corner_x = int(input("Enter the x coordinate of the upper left corner: "))
            upper_right_corner_y = int(input("Enter the y coordinate of the upper left corner: "))
            upper_right_corner = Point(x=upper_right_corner_x, y=upper_right_corner_y)

            # Check if coordinates are properly defined
            if bottom_left_corner_x >= upper_right_corner_x:
                return "You didn't put the coordinates properly"
            elif bottom_left_corner_y >= upper_right_corner_y:
                return "You didn't put the coordinates properly"

            width = upper_right_corner_x - bottom_left_corner_x
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
            print("Please enter a valid method: 1, 2, or 3")

    # Method to compute the area of the rectangle
    def compute_area(self):
        area = self.width * self.height
        return area

    # Method to compute the perimeter of the rectangle
    def compute_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    # Method to check if a given point lies within the rectangle
    def compute_interference_point(self, method, point):
        if method == 1:
            if self.blc_x <= point.x <= self.blc_x + self.width and \
                    self.blc_y <= point.y <= self.blc_y + self.height:
                return True
            else:
                return False

        elif method == 2:
            if self.center_point.x - (self.width / 2) <= point.x <= self.center_point.x + (self.width / 2) and \
                    self.center_point.y - (self.height / 2) <= point.y <= self.center_point.y + (self.height / 2):
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
    # Definition of the Square class
    definition: str = "A geometric form with four equal sides, in the Cartesian plane."

    # Constructor method for Square class
    def __init__(self, method):
        super().__init__(method)

        # Check if it's a square
        if self.width != self.height:
            print("A square must have equal width and height.")
        else:
            # Define methods to compute area and perimeter
            def compute_area(self):
                return super().compute_area()

            def compute_perimeter(self):
                return super().compute_perimeter()


if __name__ == "__main__":
    # Main execution
    method = int(input("Enter the method that you want (1, 2, or 3) for Rectangle: "))
    rectangle = Rectangle(method)

    # Compute and print area and perimeter of the rectangle
    print("The area is", rectangle.compute_area())
    print("The perimeter is", rectangle.compute_perimeter())

    # Check if a given point lies within the rectangle
    point = Point(x=int(input("Enter the x coordinate of the point: ")),
                  y=int(input("Enter the y coordinate of the point: ")))
    if rectangle.compute_interference_point(method, point):
        print("The point is inside the rectangle")
    else:
        print("The point is not inside the rectangle")

    print("\n")

    print("Now we are going to create a Square")

    # Create a square with user-defined method
    method = int(input("Enter the method that you want (1, 2, or 3) for Square: "))
    square = Square(method)

    # Compute and print area and perimeter of the square
    print("The area is", square.compute_area())
    print("The perimeter is", square.compute_perimeter())

    # Check if a given point lies within the square
    point = Point(x=int(input("Enter the x coordinate of the point: ")),
                  y=int(input("Enter the y coordinate of the point: ")))
    if square.compute_interference_point(method, point):
        print("The point is in the square")
    else: 
        print("The point isn't in the square")
```
### CLASS DIAGRAM

``` mermaid
classDiagram
    class Point {
        -x: float
        -y: float
        +move(new_x: float, new_y: float): void
        +reset(): void
    }
    class Rectangle {
        -bottom_left_corner: Point
        -blc_x: float
        -blc_y: float
        -width: float
        -height: float
        +compute_area(): float
        +compute_perimeter(): float
        +compute_interference_point(method: int, point: Point): bool
    }
    class Square {
        -bottom_left_corner: Point
        -blc_x: float
        -blc_y: float
        -width: float
        -height: float
        +compute_area(): float
        +compute_perimeter(): float
        +compute_interference_point(method: int, point: Point): bool
    }

    Point <|-- Rectangle
    Rectangle <|-- Square
```
## LINE

Este código es útil para trabajar con líneas en un plano cartesiano. La clase Line nos permite calcular propiedades importantes de una línea, como su longitud y pendiente. Además, podemos verificar si la línea cruza los ejes horizontal y vertical. 

``` python
import math

class Line:
    # Constructor method to initialize the Line object with start and end points
    def __init__(self, start, end):
        self.start = start  # Start point of the line
        self.end = end      # End point of the line
        self.compute_length()  # Calculate the length of the line
        self.compute_slope()   # Calculate the slope of the line
    
    # Method to compute the length of the line segment
    def compute_length(self) -> float:
        # Formula to calculate the Euclidean distance between two points
        self.length = (( ((self.end[0]- self.start[0])**2) + ((self.end[1]- self.start[1])**2)  )**(0.5))
        
    # Method to compute the slope of the line
    def compute_slope(self) -> float:
        # Calculate the change in y and x coordinates
        delta_y = self.end[1] - self.start[1]
        delta_x = (self.end[0] - self.start[0])
        # Calculate the slope using arctan and convert to degrees
        self.slope = math.atan2(delta_y, delta_x)
        self.slope = math.degrees(self.slope)
    
    # Method to check if the line segment crosses the horizontal axis
    def compute_horizontal_cross(self):
        # Check if both start and end points are below or above the x-axis
        if self.start[0] <= 0:
            if self.end[0] <= 0:
                return False
            else: return True
        elif self.end[0] <= 0:
            if self.start[0] <= 0:
                return False
            else: return True
        else: return False
    
    # Method to check if the line segment crosses the vertical axis
    def compute_vertical_cross(self):
        # Check if both start and end points are to the left or right of the y-axis
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
    # Input start and end points of the line from user
    linea= Line(start= ((int(input("Enter the x1 ")), int(input("Enter the y1: ")))), end=((int(input("Enter the x2: ")), int(input("Enter the y2: ")))))
    # Print the calculated properties of the line
    print("Length:", linea.length)
    print("Slope:", linea.slope, "°")
    print("Horizontal Intersection:", linea.compute_horizontal_cross())
    print("Vertical Intersection:", linea.compute_vertical_cross())

```

``` mermaid
classDiagram
    class Line {
        -start: Tuple[int, int]
        -end: Tuple[int, int]
        -length: float
        -slope: float
        +__init__(start: Tuple[int, int], end: Tuple[int, int]): void
        +compute_length(): void
        +compute_slope(): void
        +compute_horizontal_cross(): bool
        +compute_vertical_cross(): bool
    }
```

## LINE IN RECTANGLE

Este código en Python maneja puntos, rectángulos y cuadrados en un plano cartesiano. La clase Point representa puntos con métodos para moverlos y restablecerlos. La clase Rectangle crea rectángulos y calcula su área, perímetro y verifica si un punto está dentro. La subclase Square garantiza que los objetos sean cuadrados. Al ejecutar el programa, se solicita al usuario crear una figura, calcular sus propiedades y verificar la posición de un punto. Los resultados se imprimen en pantalla.

``` python
import math

class Point:
    # A class representing a point in a 2D space
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."

    def __init__(self, x: float=0, y: float=0):
        # Constructor to initialize a point with default or specified coordinates
        self.x = x
        self.y = y
    
    def move(self, new_x: float, new_y: float):
        # Method to move the point to new coordinates
        self.x = new_x
        self.y = new_y
    
    def reset(self):
        # Method to reset the coordinates of the point to (0, 0)
        self.x = 0
        self.y = 0

class Rectangle:
    # A class representing a rectangle in a Cartesian plane
    definition: str = "A geometric form with 4 four sides, in the Cartesian plane"

    def __init__(self, method):
        # Constructor to initialize a rectangle based on different methods
        if method == 1:
            # Method 1: Define rectangle by bottom left corner, width, and height
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x=bottom_left_corner_x, y=bottom_left_corner_y)
            
            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))
            
            self.bottom_left_corner = bottom_left_corner
            self.blc_x = bottom_left_corner_x
            self.blc_y = bottom_left_corner_x
            self.width = width
            self.height = height
        
        elif method == 2:
            # Method 2: Define rectangle by center point, width, and height
            center_point_x = int(input("Enter the x coordinate of the center: "))
            center_point_y = int(input("Enter the y coordinate of the center: "))
            center_point = Point(x=center_point_x, y=center_point_y)
            
            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))
            
            self.center_point = center_point
            self.c_x = center_point_x
            self.c_y = center_point_y
            self.width = width
            self.height = height
        
        elif method == 3:
            # Method 3: Define rectangle by bottom left and upper right corners
            bottom_left_corner_x = int(input("Enter the x coordinate of the bottom left corner: "))
            bottom_left_corner_y = int(input("Enter the y coordinate of the bottom left corner: "))
            bottom_left_corner = Point(x=bottom_left_corner_x, y=bottom_left_corner_y)
            
            upper_right_corner_x = int(input("Enter the x coordinate of the upper right corner: "))
            upper_right_corner_y = int(input("Enter the y coordinate of the upper right corner: "))
            upper_right_corner = Point(x=upper_right_corner_x, y=upper_right_corner_y)
            
            if bottom_left_corner_x >= upper_right_corner_x:
                return "You didn't properly put the coordinates"
            elif bottom_left_corner_y >= upper_right_corner_y:
                return "You didn't properly put the coordinates"
            
            width = upper_right_corner_x - bottom_left_corner_x
            height = upper_right_corner_y - bottom_left_corner_y
            
            self.bottom_left_corner = bottom_left_corner
            self.upper_right_corner = upper_right_corner
            self.blc_x = bottom_left_corner_x
            self.blc_y = bottom_left_corner_x
            self.upc_x = upper_right_corner_x
            self.upc_y = upper_right_corner_y
            self.width = width
            self.height = height
            
        elif method == 4:
            # Method 4: Define rectangle by four points
            points = [(int(input("Enter the x_1: ")), int(input("Enter the y_1: "))),
                      (int(input("Enter the x_2: ")), int(input("Enter the y_2: "))),
                      (int(input("Enter the x_3: ")), int(input("Enter the y_3: "))),
                      (int(input("Enter the x_4: ")), int(input("Enter the y_4: ")))]
            points = sorted(points)
            
            if points[0][0] == points[1][0]:
                if points[2][0] == points[3][0]:
                    if points[0][1] == points[2][1]:
                        if points[1][1] == points[3][1]:
                            width = points[2][0] - points[0][0]
                            height = points[1][1] - points[0][1]
                        else: return "Not a rectangle"
                    else: return "Not a rectangle"
                else: return "Not a rectangle"
            else: return "Not a rectangle"
        
            self.points = points
            self.width = width
            self.height = height
        
        else: 
            print("Men, please enter something valid, just 1, 2, 3, or 4")
            
    def compute_area(self):
        # Method to compute the area of the rectangle
        area = self.width * self.height
        return area
    
    def compute_perimeter(self):
        # Method to compute the perimeter of the rectangle
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
    
    def compute_interference_point(self, method, point):
        # Method to check if a point lies within the rectangle
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
        
        elif method == 4:
            if self.points[0][0] <= point.x <= self.points[2][0] and \
               self.points[0][1] <= point.y <= self.points[1][1]:
                return True
            else:
                return False
        
class Square(Rectangle):
    # A subclass of Rectangle representing a square
    definition: str = "A geometric form with 4 four equal sides, in the Cartesian plane"

    def __init__(self, method):
        # Constructor to initialize a square based on method from Rectangle
        super().__init__(method)

        if self.width != self.height:
            print("A square must have equal width and height.")
            
        else:  # If the width and height are  equal
            # Define functions to compute the area and perimeter using inheritance
            def compute_area(self):
                return super().compute_area()  # Calls the compute_area method of the superclass
            def compute_perimeter(self):
                return super().compute_perimeter()  # Calls the compute_perimeter method of the superclass
        
if __name__ == "__main__":
    # Prompt the user to input the method to create a rectangle or square
    method = int(input("Enter the method that you want (1, 2, 3 and 4): "))
    rectangle = Rectangle(method)  # Create an object of the Rectangle class according to the selected method
    
    # Print the area and perimeter of the rectangle
    print("The area is", rectangle.compute_area())
    print("The perimeter is", rectangle.compute_perimeter())

    # Prompt the user for the coordinates of a point
    point = Point(x=int(input("Enter the x coordinate of the point: ")), y=int(input("Enter the y coordinate of the point: ")))
    # Check if the point is inside the rectangle and display a corresponding message
    if rectangle.compute_interference_point(method, point):
        print("The point is in the rectangle")
    else: 
        print("The point isn't in the rectangle")
        
    print("\n")

    print("Now we are gonna do with the square")
        
    # Prompt the user to input the method to create a square
    method = int(input("Enter the method that you want (1, 2, 3 or 4) for Square: "))
    cuadrado = Square(method)  # Create an object of the Square class according to the selected method

    # Print the area and perimeter of the square
    print("The area is", cuadrado.compute_area())
    print("The perimeter is", cuadrado.compute_perimeter())

    # if the point is or not in the rectangle/ square
    point = Point(x=int(input("Enter the x coordinate of the point: ")), y=int(input("Enter the y coordinate of the point: ")))
    if cuadrado.compute_interference_point(method, point):
        print("The point is in the square")
    else: 
        print("The point isn't in the square")
```

``` mermaid
classDiagram
    class Point {
        -x: float
        -y: float
        +__init__(x: float = 0, y: float = 0): void
        +move(new_x: float, new_y: float): void
        +reset(): void
    }
    class Rectangle {
        -bottom_left_corner: Point
        -blc_x: float
        -blc_y: float
        -upper_right_corner: Point
        -upc_x: float
        -upc_y: float
        -width: float
        -height: float
        +__init__(method: int): void
        +compute_area(): float
        +compute_perimeter(): float
        +compute_interference_point(method: int, point: Point): bool
    }
    class Square {
        -bottom_left_corner: Point
        -blc_x: float
        -blc_y: float
        -upper_right_corner: Point
        -upc_x: float
        -upc_y: float
        -width: float
        -height: float
        +__init__(method: int): void
        +compute_area(): float
        +compute_perimeter(): float
        +compute_interference_point(method: int, point: Point): bool
    }

    Point <|-- Rectangle
    Rectangle <|-- Square

```

## MENU RESTAURANT

Este código es un programa que utilicé para gestionar pedidos de comida a través de un menú predefinido. El menú incluye una variedad de opciones como comidas rápidas, bebidas, postres y proteínas, cada una con su propio precio. Cuando ejecuto el programa, primero me muestra el menú. Luego, me solicita hacer pedidos en cada categoría. Si decido hacer un pedido en una categoría, el programa me pregunta cuántos elementos quiero pedir y luego me pide que especifique cada elemento individualmente. Estos pedidos se agregan a una lista. Al final, me muestra un recibo detallado que incluye todos los elementos pedidos y el precio total. Además, si el precio total del pedido supera los 60 dólares, el programa aplica automáticamente un descuento del 2%.

``` python
class Menuitem: 
    def __init__(self, name, price=0):
        # Initializes a menu item with a name and a default price.
        self.name = name
        self.price = price

    def calculate_price(self):
        # Method to calculate the price of the item.
        return self.price

class Fastfood(Menuitem):
    def __init__(self, name, fastfood):
        # Initializes a Fastfood object with a name, type of fast food, and sets the price based on the item name.
        super().__init__(name)
        self.fastfood = fastfood
        # Sets the price based on the item name.
        if name == "hamburguer":
            self.price = 15.99
        elif name == "pizza":
            self.price = 9.99
        elif name == "hotdog":
            self.price = 7.99
        elif name == "salchipapa":
            self.price = 10.99
        else:
            self.price = 0

class Desserts(Menuitem):
    def __init__(self, name, dessert):
        # Initializes a Desserts object with a name, type of dessert, and sets the price based on the item name.
        super().__init__(name)
        self.dessert = dessert
        # Sets the price based on the item name.
        if name == "cake":
            self.price = 6.99
        elif name == "icecream":
            self.price = 1.99
        elif name == "sundae":
            self.price = 6.99
        else:
            self.price = 0

class Drinks(Menuitem):
    def __init__(self, name, drink):
        # Initializes a Drinks object with a name, type of drink, and sets the price based on the item name.
        super().__init__(name)
        self.drink = drink
        # Sets the price based on the item name.
        if name == "soda":
            self.price = 4.99
        elif name == "juice":
            self.price = 3.99
        elif name == "smoothie":
            self.price = 8.99
        elif name == "water":
            self.price = 1.99
        else:
            self.price = 0

class Proteins(Menuitem):
    def __init__(self, name, protein):
        # Initializes a Proteins object with a name, type of protein, and sets the price based on the item name.
        super().__init__(name)
        self.protein = protein
        # Sets the price based on the item name.
        if name == "chicken":
            self.price = 13.99
        elif name == "fish":
            self.price = 14.99
        elif name == "meat":
            self.price = 13.99
        else:
            self.price = 0

class Order:
    menu = [
        Fastfood("hamburguer", "Fastfood"),
        Fastfood("pizza", "Fastfood"),
        Fastfood("hotdog", "Fastfood"),
        Fastfood("salchipapa", "Fastfood"),
        Desserts("cake", "Dessert"),
        Desserts("icecream", "Dessert"),
        Desserts("sundae", "Dessert"),
        Drinks("soda", "Drink"),
        Drinks("juice", "Drink"),
        Drinks("smoothie", "Drink"),
        Drinks("water", "Drink"),
        Proteins("chicken", "Protein"),
        Proteins("fish", "Protein"),
        Proteins("meat", "Protein"),
    ]

    def __init__(self):
        # Initializes an order with an empty list to store ordered items.
        self.menuitems = []

    def add_item(self, menuitem):
        # Adds an item to the order.
        self.menuitems.append(menuitem)

    def take_order(self):
        # Calculates the total price of the order.
        total_price = sum(item.price for item in self.menuitems)
        return total_price

    def print_menu(self):
        # Prints the menu options.
        print("Menu:")
        for item in self.menu:
            print("OPTION:  " +str(item.name)+ " = $" +str(item.price))
        print("IF YOUR ORDER IS MORE THAT 50 DOLLARS, YOU GET AN 2% DISCOUNT IN THE TOTAL BILLn")
        print("\n")

    def print_receipt(self):
        # Prints the order receipt, including discounts if applicable.
        print("This is your order Receipt:")
        for item in self.menuitems:
            print("-" +str(item.name)+ ": $" +str(item.price))
        total_price = self.take_order()
        if total_price > 60:
          total_price = total_price * 0.98
        print("Total: " +str(total_price))

# Example usage
order = Order()

# Prints the menu before taking orders
order.print_menu()


# Prompt user to order Fast Food
fast_food = input("Do you want to order Fast Food?: ")
if fast_food.lower() == "yes":
    fast_food_quantity = int(input("How many? "))
    for _ in range(fast_food_quantity):
        order_food = input("What do you want to order: ")
        order.add_item(Fastfood(order_food.lower(), "Fastfood"))
else:
    print("Ok, I'm going to continue")

# Prompt user to order Drinks
drinks = input("Do you want to order Drinks?: ")
if drinks.lower() == "yes":
    drinks_quantity = int(input("How many? "))
    for _ in range(drinks_quantity):
        order_drink = input("What do you want to order: ")
        order.add_item(Drinks(order_drink.lower(), "Drink"))
else:
    print("Ok, I'm going to continue")

# Prompt user to order Desserts
desserts = input("Do you want to order Desserts?: ")
if desserts.lower() == "yes":
    desserts_quantity = int(input("How many? "))
    for _ in range(desserts_quantity):
        order_dessert = input("What do you want to order: ")
        order.add_item(Desserts(order_dessert.lower(), "Dessert"))
else:
    print("Ok, I'm going to continue")
  
# Prompt user to order Proteins
proteins = input("Do you want to order Proteins?: ")
if proteins.lower() == "yes":
    proteins_quantity = int(input("How many? "))
    for _ in range(proteins_quantity):
        order_protein = input("What do you want to order: ")
        order.add_item(Proteins(order_protein.lower(), "Protein"))
else:
    print("Ok, I'm going to continue")
    print("\n")

# Print the receipt after taking all orders
order.print_receipt()
```

### Diagrama de Clases

``` mermaid
classDiagram
    class Menuitem {
        -name: string
        -price: float
        +calculate_price(): float
    }
    class Fastfood {
        -fastfood: string
        +Fastfood(name: string, fastfood: string)
    }
    class Desserts {
        -dessert: string
        +Desserts(name: string, dessert: string)
    }
    class Drinks {
        -drink: string
        +Drinks(name: string, drink: string)
    }
    class Proteins {
        -protein: string
        +Proteins(name: string, protein: string)
    }
    class Order {
        +add_item(menuitem: Menuitem)
        +take_order(): float
        +print_receipt()
    }
    Menuitem <|-- Fastfood
    Menuitem <|-- Desserts
    Menuitem <|-- Drinks
    Menuitem <|-- Proteins
    Menuitem *-- Order
```
