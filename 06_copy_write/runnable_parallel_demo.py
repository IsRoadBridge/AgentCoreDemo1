"""
顺序链
LangChain 的一个典型链条由Prompt、Model、OutputParser （可没有）组成，
然后可以通过 链（Chain） 把它们顺序组合起来，让一个任务的输出成为下一个任务的输入
意思等价于Linux里面的管道符
"""

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
from loguru import logger
import os
from dotenv import load_dotenv

from commondatastructure.CommonZip import result

load_dotenv()

chinese_promt = ChatPromptTemplate.from_messages(
    [("system","你是一个{role}"),
     ("human","{question}")]
)


english_promt = ChatPromptTemplate.from_messages(
    [("system", "You are a {role}, please answer in English."),
     ("human", "{question}")]
)

model = init_chat_model(
    model_provider = "openai",
    api_key=os.getenv("aliQwen-api"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
)

output_parser = StrOutputParser()

chain1 = chinese_promt | model | output_parser

chain2 = english_promt | model | output_parser

# 创建并行链,用于同时执行多个语言处理链
parallel_chain = RunnableParallel({
    "chinese": chain1,
    "english": chain2
})

result = parallel_chain.invoke({"role": "编程专家","question": "什么是Python中的装饰器？"})


print(result)
# 打印并行链的ASCII图形表示，LangGraph提前预告，不是本节知识点
parallel_chain.get_graph().print_ascii()
