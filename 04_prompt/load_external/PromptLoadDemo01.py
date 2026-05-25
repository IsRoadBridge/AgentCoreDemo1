
# 方式1：外部加载Prompt,将 prompt 保存为 JSON
from langchain_core.prompts import load_prompt
from langchain_core.prompts import PromptTemplate
#LangChainDeprecationWarning: The function `load_prompt` was deprecated in LangChain 1.2.21 and will be removed in 2.0.0. Use `Use `dumpd`/`dumps` from `langchain_core.load` to serialize prompts and `load`/`loads` to deserialize them.` instead.
#load_prompt将被弃用
#template = load_prompt("prompt.json", encoding="utf-8")
#print(template.format(name="张三", what="搞笑的"))
# 请张三讲一个搞笑的的故事

template = PromptTemplate.from_file("prompt.yaml", encoding="utf-8")
print(template.format(name="中文", what="Hello"))