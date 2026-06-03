1. 本地环境需要先安装uv
pip install uv
2. 创建uv项目的两种方式  第一种直接在pycharm里面选择uv创建项目，
   第二种跳到指定目录执行uv init my-project，然后用pycharm打开项目，缺vnev环境就在终端执行uv venv
3. 常用命令
uv init	在当前或指定目录初始化一个新的Python项目，会自动生成 pyproject.toml 等文件。	uv init my-project
uv add <package>	为项目添加一个或多个依赖包，并自动更新 pyproject.toml 和 uv.lock 文件。	uv add requests
uv remove <package>	从项目中移除指定的依赖包。	uv remove requests
uv sync	这是最常用的命令之一，它读取 pyproject.toml 并安装所有依赖，确保项目环境与锁文件精确一致。	uv sync
uv venv	在当前目录创建一个新的虚拟环境
