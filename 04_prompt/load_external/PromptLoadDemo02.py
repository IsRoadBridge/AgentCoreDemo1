import warnings
warnings.filterwarnings("ignore",
                        message="Core Pydantic V1 functionality isn't compatible with Python 3.14")

# 方式2：外部加载Prompt,将 prompt 保存为 yaml
from langchain_core.prompts import load_prompt
from langchain_core.prompts import PromptTemplate

#template = load_prompt("prompt.yaml", encoding="utf-8")
#print(template.format(name="年轻人", what="滑稽"))
# 请年轻人讲一个滑稽的故事




# 如果你的prompt.yaml内容只是一个字符串模板
# 例如 prompt.yaml 文件内容为： "请用{language}翻译以下内容：{text}"
template = PromptTemplate.from_file("prompt.yaml", encoding="utf-8")
print(template.format(name="中文", what="Hello"))
