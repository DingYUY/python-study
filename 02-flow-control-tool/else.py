# 在 for 或 while 循环中 break 语句可能对应一个 else 子句
# 如果循环在未执行 break 的情况下结束，else 子句将会执行

# 在 for 循环中，else 子句会在循环结束其他最后一次迭代之后，即未执行 break 的情况下被执行
# 在 while 循环中，它会在循环条件变为假值后执行。

# 在这两类循环中，当在循环被 break 终结时 else 子句 不会 被执行。 当然，其他提前结束循环的方式，如 return 或是引发异常，也会跳过 else 子句的执行。

for n in range(2, 10):
    for m in range(2, n):
        if n % m == 0:
            print(n, 'equals', m, '*', n // m)
            break
    else:
        print(n, 'is a prime number')