# 标注 是以字典形式存放在函数的 __annotations__ 属性中的而对函数的其他部分没有影响。 形参标注的定义方式是在形参名后加冒号，后面再跟一个将被求值为标注的值的表达式。 返回值标注的定义方式是加符号 ->，后面再跟一个表达式，它位于形参列表和表示 def 语句结束的冒号之间。

def f(ham: str, eggs: str = 'eggs') -> str:
    print('Annotations:', f.__annotations__)
    print('Arguments:', ham, eggs)
    return ham + 'and' + eggs

print(f('spam'))