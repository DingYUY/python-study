### 映射类型 --- 字典 dict
# 字典在其他编程语言中可能称为“联合内存”或“联合数组”。
# 与以连续整数为索引的序列不同，字典是以 键 来索引的，键可以是任何不可变类型；字符串和数字总是可以作为键
# 元组在其仅包含字符串、数字或元组时也可以作为键；如果一个元组直接或间接地包含了任何可变对象，则不可以用作键。
#  你不能使用列表作为键，因为列表可使用索引赋值、切片赋值或 append() 和 extend() 等方法进行原地修改。

# 可以把字典理解为 键值对 的集合，但字典的键必须是唯一的。花括号 {} 用于创建空字典。
# 另一种初始化字典的方式是，在花括号里输入逗号分隔的键值对，这也是字典的输出方式。

# 字典的主要操作是通过键来存储值并根据给定的键来提取值。
#  通过 del 也可以删除键值对。 如果你使用已存在的键进行存储，则与该键相关联的旧值将丢失。

# 通过下标操作 (d[key]) 提取不存在的键的值会引发 KeyError。
# 要避免在试图访问可能不存在的键时遇到这种错误，可改用 get() 方法，它会在字典不存在某个键时返回 None (或指定的默认值)。

# 对字典执行 list(d) 操作，返回该字典中所有键的列表，按插入次序排列（如需排序，请使用 sorted(d)）。检查字典里是否存在某个键，使用关键字 in。


tel = { 'jack': 4098, 'sape': 4139 }
tel['guido'] = 4127
print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
print(tel['jack']) # 4098

# print(tel['irv'])
# Traceback (most recent call last):
#   File "D:\PythonStudy\python-study\03-data-structure\dict.py", line 23, in <module>
#     print(tel['irv'])
#           ~~~^^^^^^^
# KeyError: 'irv'

print(tel.get('irv'))  # None

del tel['sape']
print(tel)  # {'jack': 4098, 'guido': 4127}

tel['irv'] = 4127
print(tel)  # {'jack': 4098, 'guido': 4127, 'irv': 4127}

print(list(tel))  # ['jack', 'guido', 'irv']

print(sorted(tel))  # ['guido', 'irv', 'jack']

print('guido' in tel)  # True

print('jack' not in tel)  # False


##  dict() 构造函数可以直接用键值对序列创建字典：
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 字典推导式可以用任意键值表达式创建字典：
print({ x: x**2 for x in (2, 4, 6) })
# {2: 4, 4: 16, 6: 36}

# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷
print(dict(sape=4139, guido=4127, jack=4098))
# {'sape': 4139, 'guido': 4127, 'jack': 4098}