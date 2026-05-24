1.访问官网下载ollma
https://ollama.com/download   检查是否安装成功：ollama --version
2. 在“系统属性” -> “高级” -> “环境变量”中，新建系统变量 OLLAMA_MODELS。
设置变量值为新的存储路径，如 D:\OllamaModels。
配置完成后重启终端或重启 Ollama 服务。
3. 安装指定大模型及命令
ollama run qwen:4b
4. 查看安装的大模型列表
ollama  list


附加：国内加速
Ollama 官方源下载很慢，推荐的解决方案是使用阿里 ModelScope（魔搭）社区的镜像。

操作步骤：

前往 ModelScope官网https://modelscope.cn/home 搜索你想要的 GGUF 格式模型。

进入模型详情页，复制其模型 ID。

在终端使用 ollama pull modelscope.cn/<复制的模型ID> 命令进行下载。例如：ollama pull modelscope.cn/Qwen/Qwen2.5-7B-Instruct-GGUF。