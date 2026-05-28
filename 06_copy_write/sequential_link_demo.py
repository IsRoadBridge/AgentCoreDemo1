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

load_dotenv()

prompt = ChatPromptTemplate(
    [("system","你是一个{role}"),
     ("human","question")]
)


model = init_chat_model(
    model_provider = "openai",
    api_key=os.getenv("aliQwen-api"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
)

output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({
    "role": "java专家",
    "question": "写一段简单java代码"
})

print(result)
print(output_parser.parse(result))
print(type(output_parser.parse(result)))