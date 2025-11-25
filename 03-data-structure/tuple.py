### 元组也是一种标准序列类型

# 元组由多个用逗号隔开的值组成
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# 元组可以嵌套：
u = t, (1, 2, 3, 4, 5)
print(u)

# 元组是不可变对象
# t[0] = 88888
# Traceback (most recent call last):
#   File "D:\PythonStudy\python-study\03-data-structure\tuple.py", line 13, in <module>
#     t[0] = 88888
#     ~^^^
# TypeError: 'tuple' object does not support item assignment

# 但它们可以包含可变对象：
v = ([1, 2, 3], [3, 2, 1])
print(v)

## 输出时，元组都要由圆括号标注，这样才能正确地解释嵌套元组。
## 输入时，圆括号可有可无，不过经常是必须的（如果元组是更大的表达式的一部分）。
## 不允许为元组中的单个元素赋值，当然，可以创建含列表等可变对象的元组。

# 虽然，元组与列表很像，但使用场景不同，用途也不同。
# 元组是 immutable （不可变的），一般可包含异质元素序列，通过解包（见本节下文）或索引访问（如果是 namedtuples，可以属性访问）。
# 列表是 mutable （可变的），列表元素一般为同质类型，可迭代访问


# 构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变
# 用一对空圆括号就可以创建空元组；只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）。
empty = ()
singleton = 'hello',   ## 注意末尾的逗号
print(len(empty))  # 0
print(len(singleton)) # 1
print(singleton)  # ('hello',)

# 语句 t = 12345, 54321, 'hello!' 是 元组打包 的例子：值 12345, 54321 和 'hello!' 一起被打包进元组。逆操作也可以
t = 12345, 54321, 'hello!'
x, y, z = t
print(x, y, z) # 12345 54321 hello!
# 称之为 序列解包 也是妥妥的，适用于右侧的任何序列。序列解包时，左侧变量与右侧序列元素的数量应相等。
# 注意，多重赋值其实只是元组打包和序列解包的组合。