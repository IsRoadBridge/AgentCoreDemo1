#集合（set） vs Java 的 HashSet
# 创建
colors = {"red", "green", "blue"}
empty_set = set()   # 注意 {} 是空字典

# 常用操作
colors.add("yellow")           # 添加
colors.remove("green")         # 删除，不存在则报错
colors.discard("purple")       # 删除，不存在不报错
if "red" in colors:            # 成员测试
    print("有红色")
other = {"blue", "yellow"}
print(colors.union(other))     # 并集
print(colors.intersection(other)) # 交集

#Python 的 frozenset 是不可变集合，可作字典键。Java 中对应 Set.of() 创建的不可变集合。

fs = frozenset([1, 2, 3])
# fs.add(4)          # 报错，不可变
d = {fs: "immutable set key"}   # 可作字典键