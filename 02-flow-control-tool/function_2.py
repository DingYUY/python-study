# 函数定义支持可变数量的参数。

# ===================== 1. 默认值参数 ======================
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



# ==================== 2. 关键字参数 ==================
# kwarg=value 形式的 关键字参数 也可以用于调用函数
def parrot(voltage, stage='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, 'volts through it. ')
    print("-- Lovely plumage, the", type)
    print("-- It's", stage, "!")

# =================== 有效调用方式 ===================
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOM')
parrot(action='VOOOOM', voltage=1000000)
parrot('a million', 'berefit of life', 'jump')
parrot('a thousand', stage='pushing up the daisies')

# =================== 无效调用方式 ===================
# parrot()                     # 缺失必需的参数
# parrot(voltage=5.0, 'dead')  # 关键字参数后存在非关键字参数
# parrot(110, voltage=220)     # 同一个参数重复的值
# parrot(actor='John Cleese')  # 未知的关键字参数

# 函数调用时，关键字参数必须跟在位置参数后面
# 所有传递的关键字参数都必须匹配一个函数接受的参数（比如，actor 不是函数 parrot 的有效参数），关键字参数的顺序并不重要。
# 这也包括必选参数，（比如，parrot(voltage=1000) 也有效）。不能对同一个参数多次赋值

# =================================
# 最后一个形参为 **name 形式时，接收一个字典， 该字典包含与函数中已定义形参对应之外的所有关键字参数
# **name 形参可以与 *name 形参（下一小节介绍）组合使用（*name 必须在 **name 前面）， *name 形参接收一个 元组，该元组包含形参列表之外的位置参数。
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Linda",
           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# 注意，关键字参数在输出结果中的顺序与调用函数时的顺序一致


# ===================== 3. 特殊参数 ===================

# ---------------- 3.1 位置或关键字参数 ----------------
# 函数定义中未使用 / 和 * 时，参数可以按位置或关键字传递给函数。

# ---------------- 3.2 仅位置参数 ---------------------
# 特定形参可以标记为 仅限位置。
# 仅限位置 时，形参的顺序很重要，且这些形参不能用关键字传递。
# 仅限位置形参应放在 / （正斜杠）前。/ 用于在逻辑上分割仅限位置形参与其它形参。如果函数定义中没有 /，则表示没有仅限位置形参。

# --------------- 3.3 仅限关键字参数 -------------------
# 把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字 形参前添加 *。

# --- demo ---
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

standard_arg(2)
# 2
standard_arg(arg=2)
# 2
pos_only_arg(1)
# 1
# pos_only_arg(arg=1) # 函数定义中有 /，仅限使用位置形参
# Traceback (most recent call last):
#   File "E:\Code Space\Python\study\base-study\02-flow-control-tool\function_2.py", line 134, in <module>
#     pos_only_arg(arg=1)
#     ~~~~~~~~~~~~^^^^^^^
# TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# kwd_only_arg(3) # 函数定义中通过 * 所指明的那样只允许关键字参数
# TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

# combined_example(1, 2, 3)
# TypeError: combined_example() takes 2 positional arguments but 3 were given

combined_example(1, 2, kwd_only=3)
# 1 2 3

combined_example(1, standard=2, kwd_only=3)
# 1 2 3

# combined_example(pos_only=1, standard=2, kwd_only=3)
# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


# 下面的函数定义中，kwds 把 name 当作键，因此，可能与位置参数 name 产生潜在冲突：
def foo(name, **kwds):
    return print('name' in kwds)

# 调用该函数不可能返回 True，因为关键字 'name' 总与第一个形参绑定
foo(1, **{'name': 2})
# TypeError: foo() got multiple values for argument 'name'
# 加上 / （仅限位置参数）后，就可以了。此时，函数定义把 name 当作位置参数，'name' 也可以作为关键字参数的键

# 换句话说，仅限位置形参的名称可以在 **kwds 中使用，而不产生歧义。

# ======================== 小结 ====================
# 以下用例决定哪些形参可以用于函数定义：
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

# 1、使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
# 2、当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。
# 3、对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。


