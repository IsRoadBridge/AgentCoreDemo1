# LangChain1.0+版本使用方式,目前主流,多模型共存


# 1.导入依赖
from pathlib import Path

from hello_ai_deepseek import YAMLConfig
from langchain_deepseek import ChatDeepSeek

import os
"""
说明：
model="deepseek-chat" 和 base_url="https://api.deepseek.com" 
刚好匹配默认的 model_provider（如 deepseek），因此无需显式传入，函数内部做了智能推导
如果切换成其他模型（如 OpenAI），若默认值不匹配，就需要显式指定 model_provider="openai"。
"""


project_root = Path(__file__).parent.parent
config_path = project_root / "config.yaml"
print(f"config_path = {config_path}")           # 打印出来看看
print(f"文件是否存在: {config_path.exists()}")   # 检查文件是否真的存在

config = YAMLConfig(config_path)   # 确保使用 config_path 变量

# 初始化模型
model = ChatDeepSeek(
    model="deepseek-chat",
    api_key=config.get_value("DEEPSEEK_API_KEY"),
)

# 简单调用
question = "你好，请介绍一下你自己"
response = model.invoke(question)
print(response.content)