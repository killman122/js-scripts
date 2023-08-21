# hash加密/解密

import hashlib

data = "python" # 这里的data是要加解密的字符串
# 创建hash对象
md5 = hashlib.md5(data.encode())# 如果没有编码,就需要在传入的字符串参数中传入编码后的数据data.encode()
# 但是如果传入的数据是已经编码后的,那么在后面就不需要使用update(传入数据加密data.encode())
# 向hash对象中添加需要使用hash运算的自符串
# md5.update(data.encode())
# 获取字符串的hash值
result = md5.hexdigest() # 但是需要注意的是在这里的hashMD5加密值是32位的,并且是全部小写,也没有被反转过的
print(result,type(result))

# 输出全部大写的MD5加密数据
print(result.upper())
# 输出全部小写的MD5加密数据
print(result.lower())

# 输出反转后的MD5加密数据
print(''.join(reversed(result)))
print(result[::-1])

# 输出反转后的MD5加密数据并转换为小写
print((result[::-1]).lower())
# 输出反转后的MD5加密数据并转换为大写
print((result[::-1]).upper())

