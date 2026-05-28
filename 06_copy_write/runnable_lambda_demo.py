"""
RunnableLambda-函数链
将普通Python函数融入Runnable流程.
"""
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from loguru import logger
import os
from dotenv import load_dotenv


load_dotenv()

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("aliQwen-api"),
    temperature=0.0,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

ai_promt = ChatPromptTemplate.from_messages(
    [("system","你是一个{role}"),
     ("human","{question}")]
)

end_promt = ChatPromptTemplate.from_messages(
    [("system","你是一个计算机"),
     ("human","{abc}-1*5的结果是多少")]
)

# ---------- 3. 定义普通Python函数（将被RunnableLambda包装）----------
def extract_number(text: str):
    """从文本中提取第一个出现的数字（整数或浮点数）"""
    import re
    match = re.search(r'\d+(?:\.\d+)?', text)
    if match:
        number = float(match.group())
        logger.info(f"从 '{text}' 中提取数字: {number}")
        # 返回字典，键名需匹配下一个prompt的变量名（这里是abc）
        return {"abc": str(number)}
    else:
        logger.warning(f"未找到数字，使用默认值0")
        return {"abc": "0"}

output_parser = StrOutputParser()

chain1 = ai_promt | model | output_parser

#first_chain = chain1.invoke({"role":"语言专家","question":"请用三种语言介绍大模型"})

# 将普通函数转换为Runnable
runnable_extract = RunnableLambda(extract_number)


chain2 = end_promt | model | output_parser


full_chain = chain1 | runnable_extract | chain2


result = full_chain.invoke({
    "role": "语言专家",
    "question": "请用三种语言介绍大模型,并输出一个数字"
})

print(result)
print("*" *50 + "\n")
print(full_chain)

