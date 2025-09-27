# 内置函数 range() 用于生成等差数列
for i in range(5):
    print(i)

# range 可以不从 0 开始，且可以按给定的步长递增（即使是负数步长）：
print(list(range(5, 10)))

print(list(range(0, 10, 3)))

print(list(range(-10, -110, -30)))

# 要按索引迭代序列，可以组合使用 range() 和 len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range (len(a)):
    print(a[i])

# range() 返回的对象在很多方面和列表的行为一样，但其实它和列表不一样。该对象只有在被迭代时才一个一个地返回所期望的列表项，并没有真正生成过一个含有全部项的列表，从而节省了空间。
# 这种对象称为可迭代对象 iterable，适合作为需要获取一系列值的函数或程序构件的参数
print(range(5)) # range(0, 5)