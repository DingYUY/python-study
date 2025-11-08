#### 列表详解

### 列表常见方法
list = ['1', '2', '3']

# list.append(x)
# 在列表末尾添加一项
list.append('4')
print(list)

# list.extend(iterable)
# 通过添加来自 iterable 的所有项来扩展列表。
list.extend(['5', '6', '7'])
print("list.extend(['5', '6', '7'])", list)  # ['1', '2', '3', '4', '5', '6', '7']

# list.insert(i, x)
# 在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素， a.insert(len(a), x) 等同于 a.append(x) 。
list.insert(1, '8')
print("list.insert(1, '8')", list) # ['1', '8', '2', '3', '4', '5', '6', '7']

# list.remove(x)
# 从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常。
list.remove('5')
print("list.remove('5')", list) # ['1', '8', '2', '3', '4', '6', '7']

# list.pop([i])
# 移除列表中给定位置上的条目，并返回该条目。 如果未指定索引号，则 a.pop() 将移除并返回列表中的最后一个条目。
a = list.pop(1)
print("list.pop(1)", list, 'a', a) # list.pop(1) ['1', '2', '3', '4', '6', '7'] a 8
b = list.pop()
print("list.pop()", list, 'b', b) # list.pop() ['1', '2', '3', '4', '6'] b 7

# list.clear()
# 移除列表中的所有项
# list.clear()
# print("list.clear()", list) # []

# list.index(x[, start[, end]])
# 返回列表中 x 首次出现位置的从零开始的索引。
# 可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数。
print('list.index', list.index('3')) # 2
print('list.index(x, start, end)', list.index('3', 1, 4)) # 2

# list.count(x)
# 返回列表中元素 x 出现的次数。
print('list.count', list.count('3'))  # 1

# list.sort(*, key=None, reverse=False)
# 就地排序列表中的元素

# list.reverse()
# 翻转列表中的元素。
list.reverse()
print('list.reverse()', list)

# list.copy()
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
# squares = list(map(lambda x: x**2, range(10)))
# print("squares", squares)

squares = [x**2 for x in range(10)]
print("squares", squares)


