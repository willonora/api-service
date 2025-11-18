import os
import json
import logging
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Utils:
    def __init__(self):
        self.config_file = 'config.json'

    def load_config(self) -> Dict:
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file '{self.config_file}' not found.")
            raise

    def save_config(self, data: Dict) -> None:
        with open(self.config_file, 'w') as f:
            json.dump(data, f, indent=4)

    def get_config(self) -> Dict:
        return self.load_config()

    def get_config_value(self, section: str, key: str) -> str:
        config = self.get_config()
        return config.get(section, {}).get(key, '')

    def get_config_value_list(self, section: str, key: str) -> List[str]:
        config = self.get_config()
        return config.get(section, {}).get(key, [])

    def get_config_value_int(self, section: str, key: str) -> int:
        config = self.get_config()
        return config.get(section, {}).get(key, 0)
```