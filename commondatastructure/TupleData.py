#Python 的元组不可变（不能增删改），常用于固定数据记录。Java 没有内置元组，常用替代方案：

# 创建
point = (10, 20)
rgb = (255, 0, 0)
single = (42,)     # 注意逗号，否则是整数

# 常用操作
x, y = point       # 解包
print(point[0])    # 索引访问
print(len(point))
# 不能修改：point[0] = 5  # 报错