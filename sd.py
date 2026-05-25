import sys
import subprocess

def debug_environment():
    print(f"当前Python解释器路径: {sys.executable}")
    try:
        import langchain_deepseek
        print(f"✅ langchain_deepseek 版本: {langchain_deepseek.__version__}")
        from langchain_deepseek import ChatDeepSeek
        print("✅ ChatDeepSeek 导入成功！")
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        print("请尝试运行: pip install langchain-deepseek")

if __name__ == "__main__":
    debug_environment()