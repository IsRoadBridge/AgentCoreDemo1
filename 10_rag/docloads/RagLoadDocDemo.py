# pip install langchain_community unstructured[docx]
# pip install -U unstructured
# pip install python-docx
# pip install regex==2026.1.14
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
# UnstructuredFileLoader  一个“万金油”加载器，能自动识别并解析 PDF、Word、PPT、Excel 等多种格式文件，特别适合处理复杂的非结构化文档
from langchain_community.document_loaders import UnstructuredFileLoader

docs = UnstructuredFileLoader(
    # 文件路径
    file_path="assets/alibaba-more.docx",
    # 加载模式:
    #   single 返回单个Document对象
    #   elements 按标题等元素切分文档
    mode="single",
).load()

print(type(docs))
print(docs)

