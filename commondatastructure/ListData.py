#python的list就是Java的arraylist,不同的是python可以混合数据类型

# 创建
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3]

# 常用操作
fruits.append('orange')          # 尾部添加
fruits.insert(1, 'blueberry')    # 指定位置插入
fruits.remove('banana')          # 删除首个匹配项
popped = fruits.pop()            # 弹出尾部元素
fruits[0] = 'avocado'            # 修改
print(fruits)
print(fruits[1:3])               # 切片
print(len(fruits))               # 长度