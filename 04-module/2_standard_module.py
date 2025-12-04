### 标准模块

# 一些模块是内嵌到解释器里面的， 它们给一些虽并非语言核心但却内嵌的操作提供接口，要么是为了效率，要么是给操作系统基础操作例如系统调入提供接口。
#  这些模块集是一个配置选项， 并且还依赖于底层的操作系统。 例如，winreg 模块只在 Windows 系统上提供。一个特别值得注意的模块 sys，它被内嵌到每一个 Python 解释器中。
#  sys.ps1 和 sys.ps2 变量定义了一些字符，它们可以用作主提示符和辅助提示符:
import sys
# print(sys.ps1)
# print(sys.ps2)
sys.ps1 = 'C> '

## 只有解释器用于交互模式时，才定义这两个变量。
# 变量 sys.path 是字符串列表，用于确定解释器的模块搜索路径。该变量以环境变量 PYTHONPATH 提取的默认路径进行初始化，如未设置 PYTHONPATH，则使用内置的默认路径。可以用标准列表操作修改该变量：
# import sys
# sys.path.append('/ufs/guido/lib/python')