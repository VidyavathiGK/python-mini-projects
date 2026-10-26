import json
import os


class ConfigManager:

  def __init__(self, filename="config.json"):
    self.filename = filename
    self.defaults = {
        "theme": "dark",
        "auto_save": True,
        "max_connections": 5,
        "timeout_seconds": 30,
    }
    self.config = self.load_config()

  def load_config(self) -> dict:
    if os.path.exists(self.filename):
      try:
        with open(self.filename, "r", encoding="utf-8") as f:
          data = json.load(f)
          # Merge with defaults to ensure missing keys are filled
          return {**self.defaults, **data}
      except json.JSONDecodeError:
        print("Error reading config file. Reverting to defaults.")
    return self.defaults.copy()

  def save_config(self):
    with open(self.filename, "w", encoding="utf-8") as f:
      json.dump(self.config, f, indent=4)
    print("Configuration saved successfully.")

  def get(self, key: str):
    return self.config.get(key)

  def set(self, key: str, value):
    self.config[key] = value
    if self.config.get("auto_save", True):
      self.save_config()


if __name__ == "__main__":
  cfg = ConfigManager()
  print("Current Theme:", cfg.get("theme"))
  cfg.set("theme", "light")
  print("Updated Theme:", cfg.get("theme"))
