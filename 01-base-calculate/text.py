# 单引号、双引号都可以表示str类型
import os.path

print('span eggs')
print("Paris rabbit got your back:)! Yay!")

# 要标示引号本身，我们需要对它进行“转义”，即在前面加一个 \
print('doesn\'t') # 单引号转义
print("doesn't") # 或者双引号
print('"Yes," they said')
print("\"Yes,\" they said")
print('"Isn\'t" they said')

# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可
# print('C:\some\name') # \n 表示换行符
print(r'C:\some\name')

# 原始字符串还有一个微妙的限制：一个原始字符串不能以奇数个 \ 字符结束；
# print(r'C:\this\will\not\work\')
# SyntaxError: unterminated string literal (detected at line 1)

# 有几种绕过此问题的方法
# 1. 使用常规字符串以及双反斜杠
print('C:\\this\\will\\work\\') # C:\this\will\work\
# 2. 将一个包含转义反斜杠的常规字符串拼接到原始字符串上
print(r'C:\this\will\work' '\\')
# windows上还可以使用os.path.join() 添加反斜杠
os.path.join(r'C:\this\will\work', '')
# 请注意虽然在确定原始字符串的结束位置时反斜杠会对引号进行“转义“，但在解析原始字符串的值时并不会发生转义。 也就是说，反斜杠会被保留在原始字符串的值中

# 字符串字面值可以跨越多行。 一种做法是使用三重引号: """...""" 或 '''...'''。
# 行结束符会自动包括在字符串中，但可以通过在行尾添加 \ 来避免此行为
print('''\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
''')

# 字符串可以用 + 合并，也可以用 * 重复
print(3 * 'un' + 'ium')

# 相邻的两个或多个字符串字面值会自动合并
print('Py' 'thon')
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
# 这项功能只能用于两个字面值，不能用于变量或表达式

# 合并多个变量，或合并变量与字面值，要用+
prefix = 'Py'
print(prefix + 'thon')

# 字符串支持 索引 （下标访问），第一个字符的索引是 0
word = 'Python'
print('word[0]', word[0])
print('word[5]', word[5])
print('word[-1]', word[-1])
print('word[-2]', word[-2])
print('word[-6]', word[-6])
# ! 注意，-0 和 0 一样，因此，负数索引从 -1 开始

# 除了索引操作，还支持 切片
# 左闭右开
# 从0号位（含）到2号位（不含）的字符
print('word[0:2]', word[0:2])
# 从 2 号位 (含) 到 5 号位 (不含) 的字符
print('word[2:5]', word[2:5])

# 切片索引默认值；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾
print('word[:2]', word[:2])
print('word[4:]', word[4:])
print('word[-2:]', word[-2:])
# 注意，输出结果包含切片开始，但不包含切片结束。因此，s[:i] + s[i:] 总是等于 s
print('word[:2]+word[2:]', word[:2] + word[2:])

#索引越界会报错
# 但是，切片会自动处理越界索引
print('word[4:42]', word[4:42])
print('word[42:]', word[42:])

# python字符串是不可变对象
# 因此，为字符串中某个索引位置赋值会报错

# 内置函数len()返回字符串长度
s = 'supercalifragilisticexpialidocious'
print('len(s)', len(s))
