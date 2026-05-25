# 示例1：两个列表
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

zipped = zip(names, scores)    # 返回 <zip object> 迭代器
print(list(zipped))            # 转换为列表查看： [('Alice', 95), ('Bob', 87), ('Charlie', 92)]

# 示例2：三个列表
ages = [25, 30, 22]
result = zip(names, scores, ages)
for name, score, age in result:   # 直接迭代解包
    print(f"{name} 成绩 {score}，年龄 {age}")

#1. 解压（unzip）
pairs = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
names, scores = zip(*pairs)   # 使用 * 解包列表
print(names)   # ('Alice', 'Bob', 'Charlie')
print(scores)  # (95, 87, 92)

#2. 处理不等长序列（默认以最短的为准）
a = [1, 2, 3]
b = ["a", "b"]
print(list(zip(a, b)))   # [(1, 'a'), (2, 'b')]  3 被忽略

# 如果想以最长的为准，使用 itertools.zip_longest
from itertools import zip_longest
print(list(zip_longest(a, b, fillvalue="?")))  # [(1, 'a'), (2, 'b'), (3, '?')]

#3. 配合 dict() 快速生成字典
keys = ["name", "age", "city"]
values = ["Alice", 25, "Beijing"]
d = dict(zip(keys, values))
print(d)   # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

#4. 并行遍历多个序列（常见于循环）
questions = ["name", "color", "fruit"]
answers = ["Alice", "blue", "apple"]
for q, a in zip(questions, answers):
    print(f"Q: {q}?  A: {a}")