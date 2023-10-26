import keyword
print(keyword.kwlist)

# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""

# 注意缩进
# 最好不要超过三层嵌套

# 多行语句
item_one = 1; item_two = 2; item_three = 3

total = item_one + \
        item_two + \
        item_three

print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

# 数字类型
'''
int (整数), 如 1, 只有一种整数类型 int,表示为长整型,没有 python2 中的 Long
bool (布尔), 如 True
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

# 字符串 string
'''
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号(''
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行。
按字面意义级联字符串，如 "his " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串的截取的' 或 """)可以指定一个多行字符串。
转义符 \。t语法格式如下:变量[头下标:尾下标:步长]
'''

# 空行
'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是 Python 语法的一部分。书写时不插入空行, Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

记住：空行也是程序代码的一部分。
'''

# 等待用户输入
'''
执行下面的程序在按回车键后就会等待用户输入：
'''
input("\n\n按下 Enter 键后退出")

# 同一行显示多条语句
'''
Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割
'''

# 多个语句构成代码组
'''
缩进相同的一组语句构成一个代码块，我们称之代码组。

像if、while、def和class这样的复合语句, 首行以关键字开始, 以冒号( : )结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。
'''

# 输出 print
'''
print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=" "
'''

# 导入 import & from ... import
'''
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
'''

# 命令行参数
'''
很多程序可以执行一些操作来查看一些基本信息,     Python可以使用-h参数查看各参数帮助信息
'''