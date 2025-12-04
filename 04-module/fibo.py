# 斐波那契数列模块

def fib(n):
    """ 写一个斐波那契数列 to n """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print() # 手动换行（这是数列后的第一个换行）
# 函数没有return，默认返回 None

def fib2(n):
    """ 返回斐波那契数列 to n """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result