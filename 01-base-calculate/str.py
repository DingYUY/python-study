# str 字符串 方法
# https://docs.python.org/zh-cn/3/library/stdtypes.html#textseq

# str.capitalize()
# 返回原字符串的副本，其首个字符大写，其余为小写。
# @param self
# @return Helloworld
print('str.capitalize', 'helloworld'.capitalize())

# str.casefold()
# 返回原字符串消除大小写的副本消除。大小写的字符串可用于忽略大小写的匹配
# @param self
# @return helloworld nihao
print('str.casefold', 'HelloWorld NiHao'.casefold())

# str.center(width, fillchar=' ', /)
# 返回长度为 width 的居中字符串。
# 使用指定的 fillchar 填充空位（默认为 ASCII 空格）。
# 如果 width 小于等于 len(s) 则返回原字符串。
print('str.center========start')
print('Python'.center(10)) #   Python
print('Python'.center(10, '-')) # --Python--
print('Python'.center(4)) # Python
print('str.center========end')

# str.count(sub[, start[, end]])
# 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。
# 可选参数 start 与 end 会被解读为切片表示法。
# 如果 sub 为空，则返回字符之间的空字符串数，即字符串的长度加一。
print('\nstr.count=========start')
print('spam, spam, spam'.count('spam'))  # 3
print('spam, spam, spam'.count('spam', 5)) # 2
print('spam, spam, spam'.count('spam', 5, 10)) # 1
print('spam, spam, spam'.count('eggs')) # 0
print('spam, spam, spam'.count('')) # 17
print('str.count=========end')

# str.encode(encoding='utf-8', errors='strict')
# 返回编码为 bytes 的字符串。
# bytes 内置类型 https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes
# @params encoding默认为utf-8; errors控制如何处理编码错误
print('nihao'.encode('utf-8', 'strict'))

# str.endswith(suffix[, start[, end]])
# 如果字符串以指定的 suffix 结束则返回 True，否则返回 False
# suffix 也可以是一个由供查找的后缀组成的元组
# 如果有可选项 start，测试将从该位置开始。 如果有可选项 end，将在该位置停止比较。 使用 start 和 end 等价于 str[start:end].endswith(suffix)。
print('\nstr.endswith========start')
print('python'.endswith('python')) # True
print('a tuple of suffixes'.endswith(('at', 'in'))) # False
print('a tuple of suffixes'.endswith(('at', 'es'))) # True
print('Python is amazing'.endswith('is', 0, 9)) # True
print('str.endswith=========end')

# str.expandtabs(tabsize = 8)
# 返回字符串的副本，其中所有的制表符会由一个或多个空格替换，具体取决于当前列位置和给定的制表符宽度。
# 每 tabsize 个字符设为一个制表位（默认值 8 时设定的制表位在列 0, 8, 16 依次类推）。
# 要展开字符串，当前列将被设为零并逐一检查字符串中的每个字符。
# 如果字符为制表符 (\t)，则会在结果中插入一个或多个空格符，直到当前列等于下一个制表位。 （制表符本身不会被复制。） 如果字符为换行符 (\n) 或回车符 (\r)，它会被复制并将当前列重设为零。 任何其他字符会被不加修改地复制并将当前列加一，不论该字符在被打印时会如何显示。
print('\nstr.expandtabs=======start')
print('01\t012\t0123\t01234'.expandtabs()) # 01      012     0123    01234
print('01\t012\t0123\t01234'.expandtabs(4)) # 01  012 0123    01234
print('01\t012\n0123\t01234'.expandtabs(4))
# 01  012
# 0123    01234
print('str.expandtabs=======end')

# str.find(sub[, start[, end]])
# 返回字符串sub在字符串str[start:end]中找到的最低索引。如果未找到，则返回-1
print('\nstr.find========start')
print('spam, spam, spam'.find('sp')) # 0
print('spam, spam, spam'.find('sp', 5)) # 6
print('str.find========end')

# str.format(*args, **kwargs)
# 执行字符串格式化操作。
# 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域。
# 每个替换域可以包含一个位置参数的数字索引，或者一个关键字参数的名称。
# 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值。
print("The sum of 1 + 2 is {0}".format(1+2)) # The sum of 1 + 2 is 3

# str.format_map(mapping, /)
# 类似于 str.format(**mapping)，不同之处在于 mapping 会被直接使用而不是复制到一个 dict。 适宜使用此方法的一个例子是当 mapping 为 dict 的子类的情况

# str.index(sub[, start[, end]])
# 类似于 find()，但在找不到子字符串时会引发 ValueError。

# str.isalnum()
# 如果字符串中的所有字符都是字母或数字且至少有一个字符，则返回 True ， 否则返回 False
# 如果 c.isalpha() ， c.isdecimal() ， c.isdigit() ，或 c.isnumeric() 之中有一个返回 True ，则字符 c 是字母或数字。
print("s11111".isalnum()) # True
print('%%%%'.isalnum()) # False

# str.isalpha()
# 如果字符串中的所有字符都为字母类并且至少有一个字符则返回 True，否则返回 False。
# 字母类字符是指在 Unicode 字符数据库中被定义为 "Letter" 的字符，即通用类别属性为 "Lm", "Lt", "Lu", "Ll" 或 "Lo" 之一的字符。
print('aaaa'.isalpha()) # True
print('111'.isalpha()) # False

# str.isascii()
# 如果字符串为空或字符串中的所有字符都是 ASCII ，返回 True ，否则返回 False 。

# str.isdecimal()
# 如果字符串中的所有字符都是十进制字符且该字符串至少有一个字符，则返回 True ， 否则返回 False

# str.isdigit()
# 如果字符串中的所有字符都是数字，并且至少有一个字符，返回 True ，否则返回 False 。

# str.isidentifier()
# 如果字符串是有效的标识符，返回 True

# str.islower()
# 如果字符串中至少有一个区分大小写的字符且此类字符均为小写则返回 True ，否则返回 False 。

# str.isnumeric()
# 如果字符串中至少有一个字符且所有字符均为数值字符则返回 True ，否则返回 False 。

# str.isprintable()
# 如果字符串中的所有字符均为可打印字符则返回 True，如果包含至少一个不可打印字符则返回 False。

# str.isspace()
# 如果字符串中只有空白字符且至少有一个字符则返回 True ，否则返回 False

# str.istitle()
# 如果字符串中至少有一个字符且为标题字符串则返回 True ，例如大写字符之后只能带非大写字符而小写字符必须有大写字符打头。 否则返回 False 。

# str.isupper()
# 如果字符串中至少有一个区分大小写的字符且此类字符均为大写则返回 True ，否则返回 False 。

# str.join(iterable, /)
# 返回一个由 iterable 中的字符串拼接而成的字符串。
print('str.join', '-'.join('abc')) # a-b-c

# str.ljust(width, fillchar=' ', /)
# 返回长度为 width 的字符串，原字符串在其中靠左对齐。
# 使用指定的 fillchar 填充空位 (默认使用 ASCII 空格符)。 如果 width 小于等于 len(s) 则返回原字符串的副本。
print('str.ljust', 'abc'.ljust(10, '@')) # abc@@@@@@@

# str.lower()
# 返回原字符串的副本，其所有区分大小写的字符均转换为小写

# str.lstrip(chars=None, /)
# 返回原字符串的副本，移除其中的前导字符。
# chars 参数为指定要移除字符的字符串。
# 如果省略或为 None，则 chars 参数默认移除空白符。
# 实际上 chars 参数并非指定单个前缀；而是会移除参数值的所有组合:
print('   spacious   '.lstrip()) # spacious
print('www.example.com'.lstrip('cmowz.')) # example.com
#  str.removeprefix() ，该方法将删除单个前缀字符串，而不是全部给定集合中的字符。
print('Arthur: three!'.lstrip('Arthur: '))  # 'ee'
print('Arthur: three!'.removeprefix('Arthur: ')) # 'three!'


# str.partition(sep, /)
# 在 sep 首次出现的位置拆分字符串，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。 如果分隔符未找到，则返回的 3 元组中包含字符本身以及两个空字符串。
print('Arthur: three!'.partition(':')) # ('Arthur', ':', ' three!')


# str.removesuffix(suffix, /)
# 如果字符串以 suffix 字符串结尾，并且 suffix 非空，返回 string[:-len(suffix)]。 否则，返回原始字符串的副本
print('MiscTests'.removesuffix('Tests'))  # Misc
print('TmpDirMixin'.removesuffix('Tests')) # TmpDirMixin


# str.replace(old, new, /, count=-1)
# 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new。 如果给出了 count，则只替换前 count 次出现。 如果 count 未指定或为 -1，则全部替换
print('abcdabcdabcd'.replace('a', 'e')) # ebcdebcdebcd
print('abcdabcdabcd'.replace('a', 'e', 2)) # ebcdebcdabcd

# str.rfind(sub[, start[, end]])
# 返回子字符串 sub 在字符串内被找到的最大（最右）索引，这样 sub 将包含在 s[start:end] 当中。 可选参数 start 与 end 会被解读为切片表示法。 如果未找到则返回 -1。
print('abcdabcdabcd'.rfind('abcd')) # 8

# str.rindex(sub[, start[, end]])

# str.rjust(width, fillchar=' ', /)
# 返回长度为 width 的字符串，原字符串在其中靠右对齐。 使用指定的 fillchar 填充空位 (默认使用 ASCII 空格符)。 如果 width 小于等于 len(s) 则返回原字符串的副本。

# str.rpartition(sep, /)
# 在 sep 最后一次出现的位置拆分字符串，返回一个 3 元组，其中包含分隔符之前的部分、分隔符本身，以及分隔符之后的部分。 如果分隔符未找到，则返回的 3 元组中包含两个空字符串以及字符串本身。

# str.rsplit(sep=None, maxsplit=-1)
print('sssss-aaa-vvvv'.rsplit('-')) # ['sssss', 'aaa', 'vvvv']
print('sssss-aaa-vvvv'.rsplit('-', 1)) # ['sssss-aaa', 'vvvv']

# str.rstrip(chars=None, /)
# 返回原字符串的副本，移除其中的末尾字符。
# chars 参数为指定要移除字符的字符串。
# 如果省略或为 None，则 chars 参数默认移除空白符。
# 实际上 chars 参数并非指定单个后缀；而是会移除参数值的所有组合:
print('   spacious   '.rstrip())  #    spacious
print('mississippi'.rstrip('ipz')) # mississ

# str.split(sep=None, maxsplit=-1)
# 返回一个由字符串内单词组成的列表，使用 sep 作为分隔字符串。 如果给出了 maxsplit，则最多进行 maxsplit 次拆分（因此，列表最多会有 maxsplit+1 个元素）。 如果 maxsplit 未指定或为 -1，则不限制拆分次数（进行所有可能的拆分）。
# 无需多言，都懂


# str.splitlines(keepends=False)
# 返回由原字符串中各行组成的列表，在行边界的位置拆分。 结果列表中不包含行边界，除非给出了 keepends 且为真值。
print('ab c\n\nde fg\rkl\r\n'.splitlines())  # ['ab c', '', 'de fg', 'kl']
print('ab c\n\nde fg\rkl\r\n'.splitlines(keepends=True)) # ['ab c\n', '\n', 'de fg\r', 'kl\r\n']


# str.startswith(prefix[, start[, end]])
# 如果字符串以指定的 prefix 开始则返回 True，否则返回 False。 prefix 也可以为由多个供查找的前缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 如果有可选项 end，将在所指定位置停止比较。
# 无需多言


# str.strip(chars=None, /)
# 返回原字符串的副本，移除其中的前导和末尾字符。
# chars 参数为指定要移除字符的字符串。
# 如果省略或为 None，则 chars 参数默认移除空白符。
# 实际上 chars 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合:


# str.swapcase()
# 返回原字符串的副本，其中大写字符转换为小写，反之亦然


# str.title()
# 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写


# str.translate(table, /)
# 返回原字符串的副本，其中每个字符按给定的转换表进行映射


# str.upper()
# 返回原字符串的副本，其中所有区分大小写的字符均转换为大写


# str.zfill(width, /)
# 返回原字符串的副本，在左边填充 ASCII '0' 数码使其长度变为 width。 正负值前缀 ('+'/'-') 的处理方式是在正负符号 之后 填充而非在之前。 如果 width 小于等于 len(s) 则返回原字符串的副本。


