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



