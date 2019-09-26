# Demostrating that Objects are mutable
# Accecsing global variables with self can modify those variables for each particular instance only
# But Modifying global variables with class_Name can modify the whole class permanently
# and objects created after modification will have modified global variables.

# self VS ClassName

print("Modified a particular instance of the class")


class Rectangle:
    height = 0
    width = 0

    def change(self, modifyHeight, modifyWidth):
        self.height += modifyHeight
        self.width += modifyWidth


r1 = Rectangle()
print("%d,%d" % (r1.height, r1.width))
r1.height = 100
r1.change(50, 60)

print("%d,%d" % (r1.height, r1.width))

r2 = Rectangle()
print("%d,%d" % (r2.height, r2.width))

# self VS ClassName

print("Modified the whole class global variables forever")


class Rectangle:
    height = 0
    width = 0

    def change(self, modifyHeight, modifyWidth):
        Rectangle.height += modifyHeight
        Rectangle.width += modifyWidth


r1 = Rectangle()
print("%d,%d" % (r1.height, r1.width))
r1.height = 100
r1.change(50, 60)

print("%d,%d" % (r1.height, r1.width))

r2 = Rectangle()
print("%d,%d" % (r2.height, r2.width))
