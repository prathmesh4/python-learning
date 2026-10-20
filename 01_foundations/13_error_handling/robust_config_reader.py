import json
import os

CONFIG_FILE = "config.json"
defaults = {
    "volume": 50,
    "theme": "dark",
    "notifications": True
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print("Config file not found. Creating defaults.")

        with open(CONFIG_FILE, "w") as file:
            json.dump(defaults, file, indent=4)

        return defaults.copy()

    try:
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
    except (json.JSONDecodeError, UnicodeDecodeError):
        print("Warning: bad JSON, using defaults")
        return defaults.copy()
    except OSError as error:
        print(f"Warning: cannot read config ({error}). Using defaults.")
        return defaults.copy()

    if not isinstance(config, dict):
        print("Warning: config must be a JSON object. Using defaults.")
        return defaults.copy()

    result = {}
    for key, default_value in defaults.items():
        value = config.get(key, default_value)
        if type(value) is not type(default_value):
            print(f"Warning: invalid type for '{key}'. Using default.")
            value = default_value

        result[key] = value
    return result

config = load_config()

print("\nReturned config:", config)