# 函数定义支持可变数量的参数。

# 默认值参数
# 为参数指定默认值是非常有用的方式。调用函数时，可以使用比定义时更少的参数
def ask_ok(prompt, retries=4, remind='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in { 'y', 'ye', 'yes' }:
            return True
        if reply in { 'n', 'no', 'nop', 'nope' }:
            return False
        retries = retries - 1
        if retries < 0:
        # raise 关键字用于引出异常
            raise ValueError('invalid user response')
        print(remind)

# 只给出必选实参：
# ask_ok('Do you really want to quit?')
# 给出一个可选实参：
# ask_ok('OK to overwrite the file?', 2)
# 给出所有实参：
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# 默认值在 定义 作用域里的函数定义中求值
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f2(1))
print(f2(''))