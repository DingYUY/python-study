squares = [1, 4, 9, 16, 25]

# 列表也支持索引和切片
print('squares[0]:', squares[0]) # 1
print('squares[-1]:', squares[-1]) # 25
print('squares[-3:]', squares[-3:]) # [9, 16, 25]

# 支持合并
print(squares + [36, 49, 64, 81, 100]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 添加，类似push
squares.append(216)
print(squares) # [1, 4, 9, 16, 25, 216]

# Python 中的简单赋值绝不会复制数据。 当你将一个列表赋值给一个变量时，该变量将引用 现有的列表。
rgb = ['red', 'green', 'blue']
rgba = rgb
print(id(rgba) == id(rgb)) # True
rgb.append('orange')
print(rgba)

# 切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 浅拷贝
correct_rgba = rgba[:]
correct_rgba[-1] = 'grey'
print(correct_rgba[-1])
print(correct_rgba)
print(rgba)

# 为切片赋值可以改变列表大小，甚至清空整个列表
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
letters[2:5] = ['C', 'D', 'E']
print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g', 'h', 'i', 'j']
letters[2:5] = []
print(letters)  # ['a', 'b', 'f', 'g', 'h', 'i', 'j']
letters[:] = []
print(letters) # []
