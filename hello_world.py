# print("hello" + " my son" + " good morning!")# 字符串连接
# print("我是第一行\n我是第二行")# \n换行符
# print('Let\'s go')# \' \"单双引号转义
# print("""
#         真的
#         不是
#         不会
#         而是
#         不想""")# 三引号跨行字符串

# message="hello Python world!"
# print(message)

# message="Hello Python Crash Course world!"
# print(message)

# message='python '
# message.strip()

url='https://nostarch.com'
mes_front=url.removeprefix('https://')#移除前缀
mes_back=url.removesuffix('.com')#移除后缀
print(mes_front)
print(mes_back)