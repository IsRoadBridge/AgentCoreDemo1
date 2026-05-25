import asyncio
import aiofiles

# 1. 超时控制
async def fetch_data():
    await asyncio.sleep(3)
    return "数据"

async def main():
    try:
        result = await asyncio.wait_for(fetch_data(), timeout=2)
    except asyncio.TimeoutError:
        print("任务超时！")

#2. 异步上下文管理器（如异步文件/网络连接）

# async def read_file_async(path):
#     async with aiofiles.open(path, 'r') as f:
#         content = await f.read()
#     return content
async def read_file_async(file_path: str, encoding: str = "utf-8"):
    """异步读取文件内容"""
    async with aiofiles.open(file_path, "r", encoding=encoding) as f:
        content = await f.read()
    print(f"文件长度: {len(content)} 字符")
    return content

#3. 异步生成器（async for）
async def counter(limit):
    for i in range(limit):
        await asyncio.sleep(0.5)
        yield i

async def main2():
    async for num in counter(5):
        print(num)   # 每 0.5 秒打印一个数字

if  __name__ == '__main__':
    #asyncio.run(main())  # 正确：启动事件循环并运行 main 协程
    #asyncio.run(main2())
    content = asyncio.run(read_file_async(r"C:\Users\桥哥1\PycharmProjects\AgentCoreDemo1\部署ollma.md", encoding="utf-8"))
    print(content)