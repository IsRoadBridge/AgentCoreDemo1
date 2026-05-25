from pathlib import Path
# pyrefly: ignore [missing-source-for-stubs]
import yaml


class YAMLConfig:
    def __init__(self, path):
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(f"配置文件 {path} 不存在")

        with open(self.path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)

    def get_value(self, key, default=None):
        """安全获取配置值"""
        return self.config.get(key, default)