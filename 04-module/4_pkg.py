### 包

# 包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式。 例如，模块名 A.B 表示名为 A 的包中名为 B 的子模块。 就像使用模块可以让不同模块的作者不必担心彼此的全局变量名一样，使用带点号模块名也可以让 NumPy 或 Pillow 等多模块包的作者也不必担心彼此的模块名冲突。
# 假设要为统一处理声音文件与声音数据设计一个模块集（“包”）。声音文件的格式很多（通常以扩展名来识别，例如：.wav，.aiff，.au），因此，为了不同文件格式之间的转换，需要创建和维护一个不断增长的模块集合。为了实现对声音数据的不同处理（例如，混声、添加回声、均衡器功能、创造人工立体声效果），还要编写无穷无尽的模块流。
#
# 下面这个分级文件树展示了这个包的架构：
# sound/                          最高层级的包
#       __init__.py               初始化 sound 包
#       formats/                  用于文件格式转换的子包
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  用于音效的子包
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  用于过滤器的子包
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

## 导入包时，Python 搜索 sys.path 里的目录，查找包的子目录。
# 需要有 __init__.py 文件才能让 Python 将包含该文件的目录当作包来处理（除非使用 namespace package，这是一个相对高级的特性）。
# 这可以防止重名的目录如 string 在无意中屏蔽后继出现在模块搜索路径中的有效模块。
# 在最简单的情况下，__init__.py 可以只是一个空文件，但它也可以执行包的初始化代码或设置 __all__ 变量，这将在稍后详细描述。

## 注意，使用 from package import item 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。import 语句首先测试包中是否定义了 item；如果未在包中定义，则假定 item 是模块，并尝试加载。如果找不到 item，则触发 ImportError 异常。
## 相反，使用 import item.subitem.subsubitem 句法时，除最后一项外，每个 item 都必须是包；最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量。


### 6.4.1 从包中导入*




### 6.4.2 相对导入
# 这些导入使用前导点号来表示相对导入所涉及的当前包和上级包。 例如对于 surround 模块，可以使用:
# from . import echo
# from .. import formats
# from ..filters import equalizer







