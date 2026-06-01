双击 Shift	全局搜索（文件、类、设置、操作）
Ctrl + E	最近打开的文件
Ctrl + Alt + L	格式化代码（对齐、缩进）
Ctrl + Alt + O	优化导入（去掉无用的 import）
Alt + Enter	万能修复（导包、补异常、生成方法等）

result["messages"][-1]	从列表中取最后一个元素。-1 是 Python 的特殊索引，表示倒数第一个元素。
result["messages"][-1].content	取出的最后一个元素是一个消息对象，这个对象有一个属性叫 content，它存储了消息的文本内容。

# 索引：正数从左到右（0开始），负数从右到左（-1是最后一个）
first = my_list[0]
last = my_list[-1]
second_last = my_list[-2]

# 切片：获取子列表 [起始索引:结束索引（不含）]
sub = my_list[1:4]      # 索引1,2,3
copy = my_list[:]       # 整个列表的副本

# 常用方法
my_list.append(x)       # 尾部添加
my_list.extend([a,b])   # 合并列表
len(my_list)            # 长度

numerate(messages)	遍历列表时同时获得索引和元素
msg.__class__	获取对象所属的类
.__name__	获取类的名称字符串
hasattr(obj, 'attr')	检查对象是否有指定属性
msg.tool_calls	直接访问属性（如果对象没有该属性会报错，但前面用 hasattr 保证了安全）
msg.content[:80]	字符串切片，取前 80 个字符
f"...{variable}..."	f-string 格式化字符串，将变量嵌入 {} 中