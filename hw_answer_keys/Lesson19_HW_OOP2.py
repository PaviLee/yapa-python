class Shape:
    def __init__(self, num_of_sides, color):
        self.num_of_sides = num_of_sides
        self.color = color

    def get_num_of_sides(self):
        return self.num_of_sides

    def get_color(self):
        return self.color


shape1 = Shape(3, "red")
print(shape1.num_of_sides)
print(shape1.color)

shape2 = Shape(4, "yellow")
print(shape2.num_of_sides)
print(shape2.color)
