# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587

import dashscope
from http import HTTPStatus

from langchain_community.embeddings import OllamaEmbeddings

input_text = "衣服的质量杠杠的"

# resp = dashscope.TextEmbedding.call(
#     model="text-embedding-v4",
#     input=input_text,
# )
#
# if resp.status_code == HTTPStatus.OK:
#     print(resp)


embeddings = OllamaEmbeddings(
    model="bge-m3",    # 使用BGE-M3模型，效果非常好
    base_url="http://localhost:11434"  # Ollama的默认地址，通常不需要修改
)

query_result = embeddings.embed_query(input_text)
print(query_result)