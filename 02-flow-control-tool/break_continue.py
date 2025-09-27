# break 语句将跳出最近的一层 for 或 while 循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * { n // x}")
            break


# continue 语句将继续执行循环的下一次迭代:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")