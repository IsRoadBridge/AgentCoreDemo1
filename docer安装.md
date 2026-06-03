1. windows环境准备及验证
wsl --install
wsl --version
2. 去官网下载并安装docker，验证docker是否安装成功
docker run hello-world

3. 在 docker-compose.yml 文件所在目录执行以下命令，即可一键启动：
docker-compose up -d