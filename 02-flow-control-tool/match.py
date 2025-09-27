# match 语句接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较。
# 类似 Switch 语句

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad Request"
#         case 404:
#             return "Not Found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with internet"

# 可以用 | （“或”）将多个字面值组合到一个模式
# case 401 | 403 | 404:
#     return "Not allowed"

# 形如解包赋值的模式可被用于绑定变量
# point是一个(x, y)元组
# match point:
#     case (0, 0):
#         print('Origin')
#     case (0, y):
#         print(f"Y={y}")
#     case (x, 0):
#         print(f"X={x}")
#     case (x, y):
#         print(f"X={x}, Y={y}")
#     case _:
#         raise ValueError("Not a point")
# 请仔细学习此代码！第一个模式有两个字面值，可视为前述字面值模式的扩展。接下来的两个模式结合了一个字面值和一个变量，变量 绑定 了来自主语（point）的一个值。第四个模式捕获了两个值，使其在概念上与解包赋值 (x, y) = point 类似。

# 如果用类组织数据，可以用“类名后接一个参数列表”这种很像构造器的形式，把属性捕获到变量里
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# def where_is(point):
#     match point:
#         case Point(x = 0, y = 0):
#             print("Origin")
#         case Point(x = 0, y = y):
#             print(f"Y={y}")
#         case Point(x = x, y = 0):
#             print(f"X={x}")
#         case Point():
#             print("somewhere else")
#         case _:
#             print("Not a point")

# 一些内置类（如 dataclass）为属性提供了一个顺序，此时，可以使用位置参数。自定义类可通过在类中设置特殊属性 __match_args__，为属性指定其在模式中对应的位置。
# 若设为 ("x", "y")，则以下模式相互等价（且都把属性 y 绑定到变量 var）
# var = 1
#
# where_is(Point(1, var))
# where_is(Point(1, y = var))
# where_is(Point(x = 1, y = var))
# where_is(Point(y = var, x = 1))



# 通过将其视为赋值语句等号左边的一种扩展形式，来理解各个变量被设为何值。match 语句只会为单一的名称（如上面的 var）赋值，而不会赋值给带点号的名称（如 foo.bar）、属性名（如上面的 x= 和 y=）和类名（是通过其后的 "(...)" 来识别的，如上面的 Point）。
#
# 模式可以任意嵌套。举例来说，如果我们有一个由 Point 组成的列表，且 Point 添加了 __match_args__ 时，我们可以这样来匹配它

# class Point:
#     __match_args__ = ('x', 'y')
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# match points:
#     case []:
#         print("No points")
#     case [Point(0, 0)]:
#         print("The origin")
#     case [Point(x, y)]:
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")



