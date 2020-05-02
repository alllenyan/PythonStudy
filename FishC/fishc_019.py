# 编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上
def huiwenlian(str):
    str1 = str[::-1]
    if str == str1:
        print('输入的参数是回文联')
    else:
        print('输入的参数不是回文联')


huiwenlian('上海自来水来自海上')
huiwenlian('草草草草草草草操')


# 1. 编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数
def total(*str):
    for i in range(len(str)):
        letter = 0
        number = 0
        space = 0
        other = 0
        for zifu in str[i]:
            if zifu.isalpha():  # 判断是否为字母
                letter += 1
            elif zifu.isdigit():  # 判断是否为数字
                number += 1
            elif zifu == ' ':
                space += 1
            else:
                other += 1
        print('输入的字符串英文字母个数为：', letter)
        print('输入的字符串数字个数为：', number)
        print('输入的字符串空格个数为：', space)
        print('输入的字符串其他字符个数为：', other)


total('I love fishc.com.', 'I love you, you love me.')

# def count(*param):
#     length = len(param)
#     for i in range(length):
#         letters = 0
#         space = 0
#         digit = 0
#         others = 0
#         for each in param[i]:
#             if each.isalpha():
#                 letters += 1
#             elif each.isdigit():
#                 digit += 1
#             elif each == ' ':
#                 space += 1
#             else:
#                 others += 1
#         print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i + 1, letters, digit, space, others))
#
#
# count('I love fishc.com.', 'I love you, you love me.')
