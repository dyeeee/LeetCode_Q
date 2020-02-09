str1 = "abacaba"
str2 = "a"
num = (len(str1) - len(str1.replace(str2, ""))) // len(str2)

print(num)

dic = {}
dic[1] = 2
print(dic)
str3 = "333"
print(str3.count("33"))  # 就是从下标8以后开始
# (输出)	3

s = '123'

l = [1, 2, 3, 4]
print(l[-1])
