#字典（dict） vs Java 的 HashMap
# 创建
person = {"name": "Alice", "age": 30}
# 或 dict(name="Alice", age=30)

# 常用操作
person["city"] = "New York"      # 添加/修改
print(person["name"])            # 访问，键不存在抛 KeyError
age = person.get("age", 0)       # 安全访问，可设默认值
del person["age"]                # 删除键值对
if "city" in person:             # 检查键是否存在
    print(person["city"])
for k, v in person.items():      # 遍历键值对
    print(k, v)