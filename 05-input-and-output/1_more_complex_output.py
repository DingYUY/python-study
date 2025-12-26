#### 更复杂的输出格式

### 格式化输出
# 1. 使用 格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量，或字面值的 Python 表达式。
year = 2016
event = 'Referendum'
print(f'Result of the {year} {event}') # Result of the 2016 Referendum

# 2. 字符串的 str.format() 方法需要更多手动操作。 你仍将使用 { 和 } 来标记变量将被替换的位置并且可以提供详细的格式化指令，但你还需要提供待格式化的信息
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))
#  42572654 YES votes 49.67%

# 3. 还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。字符串类型还支持将字符串按给定列宽进行填充，这些方法也很有用。

## 如果不需要花哨的输出，只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串。

## str() 函数返回供人阅读的值，repr() 则生成适于解释器读取的值（如果没有等效的语法，则强制执行 SyntaxError）。
# 对于没有支持供人阅读展示结果的对象， str() 返回与 repr() 相同的值。一般情况下，数字、列表或字典等结构的值，使用这两个函数输出的表现形式是一样的。字符串有两种不同的表现形式。

# s = 'Hello World'
# print('str(s)', str(s)) # str(s) Hello World
# print('repr(s)', repr(s)) # repr(s) 'Hello World'
# print('str(1/7)', str(1/7))  # str(1/7) 0.14285714285714285

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' +repr(y) + '...'
print(s) # The value of x is 32.5, and y is 40000...

hello = 'hello, world\n'
hellos = repr(hello)
print('hellos: ', hellos) # hellos:  'hello, world\n'

print("repr((x, y, ('spam', 'eggs'))): ", repr((x, y, ('spam', 'eggs'))))
#(32.5, 40000, ('spam', 'eggs'))


### 7.1.1格式化字符串字面值

# 格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内

# 格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。下例将 pi 舍入到小数点后三位
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
table = { 'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678 }
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678


# 还有一些修饰符可以在格式化前转换值。 '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()：
animals = 'eels'
print(f'My hovercraft is full of {animals}.') # My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.') # My hovercraft is full of eels.


# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')



### 7.1.2字符串 format() 方法

# str.format() 方法的基本用法如下所示：
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

# 花括号及之内的字符(称为格式字段)被替换为传递给 str.format() 方法的对象。
# 花括号中的数字表示传递给 str.format() 方法的对象所在的位置。
print('{0} and {1}'.format('spam', 'eggs')) # spam and eggs
print('{1} and {0}'.format('spam', 'eggs')) # eggs and spam

# str.format() 方法中使用关键字参数名引用值。
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

# 位置参数和关键字参数可以任意组合：
print('The Story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
# The Story of Bill, Manfred, and Georg.

# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成。
table1 = { 'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678 }
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table1))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# 这也可以通过将 table 字典作为采用 ** 标记的关键字参数传入来实现
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table1))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# 与内置函数 vars() 一同使用时这种方式非常实用，它将返回一个包含所有局部变量的字典：
table2 = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k + '};' for k in table2.keys()])
print(message.format(**table2))
# __name__: __main__; __doc__: None; __package__: None; __loader__: <_frozen_importlib_external.SourceFileLoader object at 0x0000020BA98A18B0>; __spec__: None; __builtins__: <module 'builtins' (built-in)>; __file__: D:\PythonStudy\python-study\05-input-and-output\1_more_complex_output.py; __cached__: None; year: 2016; event: Referendum; yes_votes: 42572654; total_votes: 85705149; percentage: 0.496733912684756; x: 32.5; y: 40000; s: The value of x is 32.5, and y is 40000...; hello: hello, world
# ; hellos: 'hello, world\n'; math: <module 'math' (built-in)>; table: {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}; name: Dcab; phone: 7678; animals: eels; bugs: roaches; count: 13; area: living room; table1: {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678};

# 举个例子，以下几行代码将产生一组整齐的数据列，包含给定的整数及其平方与立方:
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000



### 7.1.3 手动格式化字符串

# 下面是使用手动格式化方式实现的同一个平方和立方的表：
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意上一行 end 的使用
    print(repr(x*x*x).rjust(4))
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# （注意，每列之间的空格是通过使用 print() 添加的：它总在其参数间添加空格。）
# 字符串对象的 str.rjust() 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。
# 同类方法还有 str.ljust() 和 str.center() 。
# 这些方法不写入任何内容，只返回一个新字符串，如果输入的字符串太长，它们不会截断字符串，而是原样返回；虽然这种方式会弄乱列布局，但也比另一种方法好，后者在显示值时可能不准确（如果真的想截断字符串，可以使用 x.ljust(n)[:n] 这样的切片操作 。）

# 另一种方法是 str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号
print('12'.zfill(5))  # 00012
print('-3.14'.zfill(7)) # -003.14
print('3.14159265359'.zfill(5)) # 3.14159265359



### 7.1.4旧式字符串格式化方法

# % 运算符 (求余) 也可被用于字符串格式化。 给定 format % values (其中 format 是一个字符串)，则 format 中的 % 转换占位符将以 values 中的零个或多个元素来替换。 此操作通常称为字符串插值。
import math
print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.