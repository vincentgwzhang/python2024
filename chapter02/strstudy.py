str1 = 's1'

str2 = '''hello
world
2024
'''

print(str2)

str4 = 'It\'s a cDebian 3.0at'
print(str4)


print('abc' * 3)
print('abc'[-1])
print('0123456789'[0:4])
print('0123456789'[0:9:2]) # 第三个参数的意思是说能隔几个取，默认就是1,就是连续
print('0123456789'[::2]) # 第三个参数的意思是说能隔几个取，默认就是1,就是连续

# 下面的结果是一样的
print('0123456789'[::1])
print('0123456789'[::])
print('0123456789'[0:10:1])
print('0123456789')

# reverse
print('0123456789'[::-1])
