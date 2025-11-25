### 集合
## 集合是由不重复元素组成的无序多项集。
## 基本用法包括成员检测和消除重复元素。
## 集合对象还支持合集、交集、差集和对称差集等数学运算。

# 创建集合用花括号或 set() 函数。
# ！！！注意，创建空集合只能用 set()，不能用 {}，{} 创建的是空字典

basket = { 'apple', 'orange', 'apple', 'pear', 'orange', 'banana' }
print(basket)
# {'pear', 'apple', 'banana', 'orange'}
# 显示重复项已被移除


# 快速成员检测
print('orange' in basket)  # True
print('crabgrass' in basket)  # False


# 演示针对两个单词中独有的字母进行集合运算
a = set('abracadabra')
b = set('alacazam')
# a 中独有的字母
print('a', a)  # {'a', 'b', 'r', 'd', 'c'}
print('b', b)  # {'l', 'a', 'm', 'z', 'c'}
# 存在于 a 中但不存在于 b 中的字母
print('a - b', a - b)  # {'r', 'd', 'b'}
# 存在于 a 或 b 中或两者中皆有的字母
print('a | b', a | b)  # {'a', 'c', 'r', 'l', 'd', 'b', 'm', 'z'}
# 同时存在于 a 和 b 中的字母
print('a & b', a & b)  # {'a', 'c'}
# 存在于 a 或 b 中但非两者中皆有的字母
print('a ^ b', a ^ b)  # {'l', 'm', 'b', 'd', 'z', 'r'}

## 与 列表推导式 类似，集合也支持推导式：
a = { x for x in 'abracadabra' if x not in 'abc' }
print(a)  # {'d', 'r'}

