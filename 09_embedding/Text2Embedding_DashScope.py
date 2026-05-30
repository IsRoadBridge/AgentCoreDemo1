"""
https://bailian.console.aliyun.com/cn-beijing/?tab=api#/api/?type=model&url=2587654
pip install langchain-community dashscope
"""

from langchain_community.embeddings import DashScopeEmbeddings, OllamaEmbeddings

# embeddings = DashScopeEmbeddings(
#     model="text-embedding-v4",
#     # other params...
# )

embeddings = OllamaEmbeddings(
    model="bge-m3",    # 使用BGE-M3模型，效果非常好
    base_url="http://localhost:11434"  # Ollama的默认地址，通常不需要修改
)
text = "This is a test document."

query_result = embeddings.embed_query(text)
print("文本向量长度：", len(query_result), sep='')
#
doc_results = embeddings.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
print(doc_results)
print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')