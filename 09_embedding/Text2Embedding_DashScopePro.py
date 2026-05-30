import dashscope
import json
import os
from http import HTTPStatus

# Embedding 文本向量化

# 调用多模态embedding模型接口进行向量编码
# https://bailian.console.aliyun.com/?productCode=p_efm&tab=model#/model-market/all?capabilities=ME
# resp = dashscope.MultiModalEmbedding.call(
#     model="tongyi-embedding-vision-plus",  # 支持 v1 或 v2
#     dashscope_api_key=os.getenv("aliQwen-api"),  # 从环境变量读取
#     input=[{"text": "尚硅谷AI"}]
# )
#
# result = "";
#
# # 处理模型返回结果，提取关键信息并格式化输出
# if resp.status_code == HTTPStatus.OK:
#     result = {
#         "status_code": resp.status_code,
#         "request_id": getattr(resp, "request_id", ""),
#         "code": getattr(resp, "code", ""),
#         "message": getattr(resp, "message", ""),
#         "output": resp.output,
#         "usage": resp.usage
#     }
#     print(json.dumps(result, ensure_ascii=False, indent=4))
#
# print("=================================")
# print()
#
# # result 就是你已经拿到的完整 dict
# embedding_values = result["output"]["embeddings"][0]["embedding"]
# print(embedding_values)
# print("=================================")
# print("=================================")
# # 只打印 embedding 数组
# print(json.dumps(embedding_values, ensure_ascii=False))


import json
from langchain_community.embeddings import OllamaEmbeddings

# 1. 初始化本地嵌入模型
embeddings = OllamaEmbeddings(
    model="bge-m3",
    base_url="http://localhost:11434"   # Ollama 默认地址
)

input_text = "尚硅谷AI"

# 2. 调用本地模型生成向量
vector = embeddings.embed_query(input_text)   # 返回 list[float]

# 3. 构造与阿里云 API 相似的返回结构（便于原有逻辑处理）
result = {
    "status_code": 200,
    "request_id": "local-ollama",
    "code": "",
    "message": "",
    "output": {
        "embeddings": [
            {
                "embedding": vector
            }
        ]
    },
    "usage": {}   # 本地模型暂无 usage 信息
}

# 4. 打印完整结果
print(json.dumps(result, ensure_ascii=False, indent=4))

print("=================================")
print()

# 5. 提取 embedding 数组
embedding_values = result["output"]["embeddings"][0]["embedding"]
print(embedding_values)
print("=================================")
print("=================================")

# 6. 只打印 embedding 数组（JSON 格式）
print(json.dumps(embedding_values, ensure_ascii=False))