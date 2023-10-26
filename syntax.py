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