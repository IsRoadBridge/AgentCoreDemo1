核心规范

1. 命名统一

文件名：全小写字母，单词间用下划线 _ 分隔  my_module.py file_utils.py test_calculator.py（测试文件常用 test_ 前缀）

变量、函数、方法：小写字母 + 下划线（snake_case），例如 user_name、get_data。

常量：全大写 + 下划线，例如 MAX_COUNT = 100。

类名：首字母大写单词拼接（CapWords），例如 class UserInfo。

私有属性/方法：前导一个下划线，例如 _internal_func。

避免使用单字符变量（循环中的 i, j, k 除外），避免与内置名称重名。

2. 缩进与格式

使用 4 个空格缩进，不用 Tab
每行尽量不超过 79 或 88 字符
运算符、逗号后保留适当空格
使用空行分隔模块、类、函数
导入规范

3. 导入顺序：标准库 -> 第三方库 -> 本地模块
避免 from xxx import *
一个导入一行，必要时分组
注释与文档

4. 复杂逻辑写注释，废话注释不要写
公共函数、类、模块建议写 docstring
注释说明“为什么”，不重复“代码做了什么”
函数设计

5. 单个函数职责单一
参数不要过多，通常不超过 5 个
返回值风格统一，不要时而返回 None 时而返回对象
尽量避免过深嵌套，必要时提前返回
异常处理

6. 不要裸写 except:
只捕获明确的异常类型
不要吞掉异常，必要时记录日志
异常信息要有上下文，便于排查
类型与可读性

7. 新项目建议使用类型注解
布尔判断写清楚，避免晦涩写法
避免魔法数字，提取为常量
面向对象规范

8. 类要有明确职责，不要“万能类”
公共接口稳定，内部实现尽量封装
简单数据结构优先考虑 dataclass
日志与调试

9. 不要大量使用 print
使用 logging
日志级别区分清楚：debug/info/warning/error
工程化工具

格式化：black
静态检查：ruff
类型检查：mypy
提交前自动检查：pre-commit
推荐代码风格示例

from dataclasses import dataclass


MAX_RETRY_COUNT = 3


@dataclass
class User:
    name: str
    age: int


def get_adult_users(users: list[User]) -> list[User]:
    """返回成年用户列表。"""
    return [user for user in users if user.age >= 18]
最重要的原则

一致性优先于个人习惯
可读性优先于炫技
简单优先于复杂
规范要能落地，最好配合自动化工具执行