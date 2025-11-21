#### 列表详解

### 列表常见方法
list_demo = ['1', '2', '3']

# list_demo.append(x)
# 在列表末尾添加一项
list_demo.append('4')
print(list_demo)

# list_demo.extend(iterable)
# 通过添加来自 iterable 的所有项来扩展列表。
list_demo.extend(['5', '6', '7'])
print("list_demo.extend(['5', '6', '7'])", list_demo)  # ['1', '2', '3', '4', '5', '6', '7']

# list_demo.insert(i, x)
# 在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素， a.insert(len(a), x) 等同于 a.append(x) 。
list_demo.insert(1, '8')
print("list_demo.insert(1, '8')", list_demo) # ['1', '8', '2', '3', '4', '5', '6', '7']

# list_demo.remove(x)
# 从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。
list_demo.remove('5')
print("list_demo.remove('5')", list_demo) # ['1', '8', '2', '3', '4', '6', '7']

# list_demo.pop([i])
# 移除列表中给定位置上的条目，并返回该条目。 如果未指定索引号，则 a.pop() 将移除并返回列表中的最后一个条目。
a = list_demo.pop(1)
print("list_demo.pop(1)", list_demo, 'a', a) # list_demo.pop(1) ['1', '2', '3', '4', '6', '7'] a 8
b = list_demo.pop()
print("list_demo.pop()", list_demo, 'b', b) # list_demo.pop() ['1', '2', '3', '4', '6'] b 7

# list_demo.clear()
# 移除列表中的所有项
# list_demo.clear()
# print("list_demo.clear()", list_demo) # []

# list_demo.index(x[, start[, end]])
# 返回列表中 x 首次出现位置的从零开始的索引。
# 可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。
print('list_demo.index', list_demo.index('3')) # 2
print('list_demo.index(x, start, end)', list_demo.index('3', 1, 4)) # 2

# list_demo.count(x)
# 返回列表中元素 x 出现的次数。
print('list_demo.count', list_demo.count('3'))  # 1

# list_demo.sort(*, key=None, reverse=False)
# 就地排序列表中的元素

# list_demo.reverse()
# 翻转列表中的元素。
list_demo.reverse()
print('list_demo.reverse()', list_demo)

# list_demo.copy()
# 返回列表的浅拷贝



### 用列表实现堆栈
# 列表方法使得将列表作为栈来使用非常容易，最后添加的元素会最先被取出（“后时先出”）。
# 要将一个条目添加到栈顶，可使用 append()。 要从栈顶取出一个条目，则使用 pop() 而不必显式指定索引。
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print('stack', stack)
stack.pop()
print('stack.pop()', stack)
stack.pop()
print('stack.pop()', stack)


### 用列表实现队列
# 列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；
# 然而，列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）。
# 实现队列最好用 collections.deque，可以快速从两端添加或删除元素。
from collections import deque
queue = deque(["Eric", 'John', 'Michael'])
queue.append("James")
queue.append("Sarah")
print("queue", queue)
queue.popleft()
print("queue", queue)
queue.pop()
print("queue", queue)


### 列表推导式
# 列表推导式创建列表的方式更简洁。常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。
squares = []
for x in range(10):
    squares.append(x**2)

print("squares", squares)
# 注意，这段代码创建（或覆盖）变量 x，该变量在循环结束后仍然存在

# 下述方法可以无副作用地计算平方列表：
# squares = list_demo(map(lambda x: x**2, range(10)))
# print("squares", squares)

squares = [x**2 for x in range(10)]
print("squares", squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 列表推导式的方括号内包含以下内容：一个表达式，后面为一个 for 子句，然后，是零个或多个 for 或 if 子句。
# 结果是由表达式依据 for 和 if 子句求值计算而得出一个新列表
print("[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]", [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 等价于
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print("combs", combs)
# combs [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# 注意，上面两段代码中，for 和 if 的顺序相同。


vec = [-4, -2, 0 , 2, 4]
# 新建一个将值翻倍的列表
print("新建一个将值翻倍的列表", [x*2 for x in vec])
# [-8, -4, 0, 4, 8]
# 过滤列表以排除负数
print("过滤列表以排除负数", [x for x in vec if x >= 0])
# [0, 2, 4]
# 对所有元素应用一个函数
print("对所有元素应用一个函数", [abs(x) for x in vec])
# [4, 2, 0, 2, 4]
# 在每个元素上调用一个方法
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# strip 返回原字符串的副本，移除其中的前导和末尾字符。
print("[weapon.strip() for weapon in freshfruit]", [weapon.strip() for weapon in freshfruit])
# ['banana', 'loganberry', 'passion fruit']
# 创建一个包含 (数字, 平方) 2 元组的列表
print("[(x, x**2) for x in range(6)]", [(x, x**2) for x in range(6)])
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# 元组必须加圆括号，否则会引发错误

# 使用两个 'for' 来展平嵌套的列表
vec = [[1,2,3], [4,5,6], [7,8,9]]
print("[num for elem in vec for num in elem]", [num for elem in vec for num in elem])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式可以使用复杂的表达式和嵌套函数：
from math import pi
print("[str(round(pi, i)) for i in range(1, 6)]", [str(round(pi, i)) for i in range(1, 6)])
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']


### 嵌套的列表推导式
# 列表推导式中的初始表达式可以是任何表达式，甚至可以是另一个列表推导式
# 下面这个 3x4 矩阵，由 3 个长度为 4 的列表组成：
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# 下面的列表推导式可以转置行列
print(
    "[[row[i] for row in matrix] for i in range(4)]",
[[row[i] for row in matrix] for i in range(4)]
)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# 等价于
# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])
# 又等价于
# transposed = []
# for i in range(4):
#     # 以下 3 行实现了嵌套的列表组
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# 实际应用中，最好用内置函数替代复杂的流程语句。此时，zip() 函数更好用：
print('list(zip(*matrix))', list(zip(*matrix)))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

