def fib(n):
    """ Print a Fibonacci series less than n """
    a, b = 0, 1
    while a <n:
        print(a, end = ' ')
        a, b = b, a+b
    print()

fib(2000)

# 定义 函数使用关键字 def，后跟函数名与括号内的形参列表。函数语句从下一行开始，并且必须缩进
#
# 函数内的第一条语句是字符串时，该字符串就是文档字符串，也称为 docstring
# 利用文档字符串可以自动生成在线文档或打印版文档，还可以让开发者在浏览代码时直接查阅文档
#
# 函数在 执行 时使用函数局部变量符号表，所有函数变量赋值都存在局部符号表中
# 引用变量时，首先，在局部符号表里查找变量，然后，是外层函数局部符号表，再是全局符号表，最后是内置名称符号表
#
# 在调用函数时会将实际参数（实参）引入到被调用函数的局部符号表中；
# 因此，实参是使用 按值调用 来传递的（其中的 值 始终是对象的 引用 而不是对象的值）。 [1] 当一个函数调用另外一个函数时，会为该调用创建一个新的局部符号表
f = fib
f(100)

# 没有 return 语句的函数也有返回值
# 这个值被称为 None (是一个内置名称)。 通常解释器会屏蔽单独的返回值 None

def fib2(n): # 返回斐波那契数组直到n
    """ Return a list containing the fibonacci series up to n """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)