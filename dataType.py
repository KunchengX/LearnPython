counter = 100       # int
miles = 1000.0      # float
name = "runnoob"    # string

print(counter)
print(miles)
print(name)

"""
标准数据类型：
    Number: 
    -- int, float, bool, complex 
    -- plus +, minus -, time *, divide /, mode %, power **
    String
    -- 字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 r\ 转义特殊字符
    -- 如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r, 表示原始字符串
    -- 字符串不可改变
    bool
    -- 在比较时, Python 会将 True 视为 1, False 视为 0
    List
    -- 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
    -- 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
    -- 类似其他语言中的数组
    Tuple
    -- 元组(tuple)与列表类似,
    -- 不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
    Set
    -- Python 中的集合(Set)是一种无序、可变的数据类型, 用于存储唯一的元素
    -- 集合中的元素不会重复
    -- 在 Python 中，集合使用大括号 {} 表示，元素之间用逗号 , 分隔
    Dictionary
    -- 列表是有序的对象集合，字典是无序的对象集合。
    -- 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取
    -- key -> value 键值对
    -- 同一个字典中, key必须是唯一的
    bytes
    -- 不可变的二进制序列 (0 - 255)
"""

# 翻转字符串
def reverseWords(input):

    # 通过空格将字符串分割成列表
    inputWords = input.split(" ")

    # 翻转字符串
    # list[0]代表第一个元素， list[-1]代表最后一个元素
    # inputWords[-1::-1]有三个参数
    # 第一个参数 -1 代表最后一个元素
    # 第二个参数为空， 表示移动到末尾
    # 第三个参数 -1 代表步长，表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)
    return output

input = 'I like runnoob'
rw = reverseWords(input)
print(rw)

# Tuple 元组