"""
分支链
在LangChain中提供了类RunnableBranch来完成LCEL中的条件分支判断，它可以根据输入的不同采用不同的处理逻辑，
具体示例如下
会根据用户输入中是否包含英语、韩语等关键词，来选择对应的提示词进行处理。根据判断结果，
再执行不同的逻辑分支
"""
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from loguru import logger
from langchain_core.runnables import RunnableBranch
import os
from dotenv import load_dotenv


load_dotenv()

# 构建提示词
english_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个英语翻译专家，你叫小英"),
    ("human", "{query}")
])

japanese_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个日语翻译专家，你叫小日"),
    ("human", "{query}")
])

korean_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个韩语翻译专家，你叫小韩"),
    ("human", "{query}")
])

# 初始化模型
model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("aliQwen-api"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# ---------- 3. 定义条件判断函数 ----------
# 这些函数接收链的输入（是一个字典，包含 "query" 键），并返回布尔值
def is_japanese(inputs: dict) -> bool:
    """如果 query 中包含 '日语' 或 'japanese' 关键词，返回 True"""
    query = inputs.get("query", "").lower()
    return "日语" in query or "japanese" in query

def is_korean(inputs: dict) -> bool:
    """如果 query 中包含 '韩语' 或 'korean' 关键词，返回 True"""
    query = inputs.get("query", "").lower()
    return "韩语" in query or "korean" in query

def is_english(inputs: dict) -> bool:
    """如果 query 中包含 '英语' 或 'english' 关键词，返回 True"""
    query = inputs.get("query", "").lower()
    return "英语" in query or "english" in query


# 创建字符串输出解析器，用于处理模型输出
parser = StrOutputParser()
# 创建一个可运行的分支链，根据输入文本的语言类型选择相应的处理流程
# 返回值：RunnableBranch对象，可根据输入动态选择执行路径的可运行链
branch_chain = RunnableBranch(
    (is_japanese, japanese_prompt | model | parser),
    (is_korean, korean_prompt | model | parser),
    (is_english, english_prompt | model | parser),
    # 默认分支：如果以上条件都不满足，走英语分支（或你可以自定义一个通用回答分支）
    english_prompt | model | parser
)

# ---------- 5. 调用示例 ----------
test_queries = [
    "请帮我翻译成英语：你好世界",
    "日语：早上好怎么说？",
    "我想翻译韩语：谢谢",
    "随便翻译成法语吧"   # 不包含任何关键词，走默认分支（英语）
]

for q in test_queries:
    print(f"\n输入：{q}")
    result = branch_chain.invoke({"query": q})
    print(f"输出：{result}")