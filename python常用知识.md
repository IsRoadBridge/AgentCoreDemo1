双击 Shift	全局搜索（文件、类、设置、操作）
Ctrl + E	最近打开的文件
Ctrl + Alt + L	格式化代码（对齐、缩进）
Ctrl + Alt + O	优化导入（去掉无用的 import）
Alt + Enter	万能修复（导包、补异常、生成方法等）

numerate(messages)	遍历列表时同时获得索引和元素
msg.__class__	获取对象所属的类
.__name__	获取类的名称字符串
hasattr(obj, 'attr')	检查对象是否有指定属性
msg.tool_calls	直接访问属性（如果对象没有该属性会报错，但前面用 hasattr 保证了安全）
msg.content[:80]	字符串切片，取前 80 个字符
f"...{variable}..."	f-string 格式化字符串，将变量嵌入 {} 中