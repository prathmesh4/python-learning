from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def initialize(self):
        pass
    @abstractmethod
    def execute(self, data):
        pass
    @abstractmethod
    def cleanup(self):
        pass
    def get_name(self):
        return self.__class__.__name__

class UppercasePlugin(Plugin):
    def initialize(self):
        print("Initializing UppercasePlugin")
    def execute(self, data):
        result = data.upper()
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up UppercasePlugin")

class FilterPlugin(Plugin):
    def __init__(self, keyword):
        self.keyword = keyword
    def initialize(self):
        print(f"Initializing FilterPlugin ({self.keyword})")
    def execute(self, data):
        result = "\n".join(
            line for line in data.splitlines()
            if self.keyword.lower() not in line.lower()
        )
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up FilterPlugin")

class SortPlugin(Plugin):
    def __init__(self, reverse=False):
        self.reverse = reverse
    def initialize(self):
        print("Initializing SortPlugin")
    def execute(self, data):
        result = "\n".join(
            sorted(data.splitlines(), reverse=self.reverse)
        )
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up SortPlugin")

class NumberPlugin(Plugin):
    def initialize(self):
        print("Initializing NumberPlugin")
    def execute(self, data):
        result = "\n".join(
            f"{i}. {line}"
            for i, line in enumerate(data.splitlines(), start=1)
        )
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up NumberPlugin")

class UniquePlugin(Plugin):
    def initialize(self):
        print("Initializing UniquePlugin")
    def execute(self, data):
        result = "\n".join(dict.fromkeys(data.splitlines()))
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up UniquePlugin")

class ReversePlugin(Plugin):
    def initialize(self):
        print("Initializing ReversePlugin")
    def execute(self, data):
        result = "\n".join(
            line[::-1] for line in data.splitlines()
        )
        print(f"After {self.get_name()}: {result.replace(chr(10), ', ')}")
        return result
    def cleanup(self):
        print("Cleaning up ReversePlugin")

class Pipeline:
    def __init__(self):
        self.plugins = []
    def add_plugin(self, plugin):
        if not isinstance(plugin, Plugin):
            raise TypeError("plugin must be an instance of Plugin")
        self.plugins.append(plugin)
    def display_pipeline(self):
        print(
            "Pipeline: "
            + " → ".join(plugin.get_name() for plugin in self.plugins)
        )
    def run(self, data):
        try:
            for plugin in self.plugins:
                plugin.initialize()
            for plugin in self.plugins:
                data = plugin.execute(data)
            return data
        finally:
            for plugin in reversed(self.plugins):
                plugin.cleanup()
pipeline1 = Pipeline()
pipeline1.add_plugin(UppercasePlugin())
pipeline1.add_plugin(SortPlugin())
pipeline1.add_plugin(NumberPlugin())
pipeline1.display_pipeline()
text1 = """banana
apple
cherry
apple
date
fig
grape"""
print("Input:")
print(text1)
result1 = pipeline1.run(text1)
print("Final output:")
print(result1)

pipeline2 = Pipeline()
pipeline2.add_plugin(FilterPlugin("error"))
pipeline2.add_plugin(UniquePlugin())
pipeline2.add_plugin(SortPlugin())
text2 = """INFO: Server started
ERROR: Connection failed
INFO: Server started
WARNING: High memory
ERROR: Disk failure
INFO: Request completed
WARNING: High memory
INFO: Backup complete"""
print("Second pipeline:")
pipeline2.display_pipeline()
print("Input:")
print(text2)
result2 = pipeline2.run(text2)
print("Final output:")
print(result2)

pipeline3 = Pipeline()
pipeline3.add_plugin(ReversePlugin())
text3 = """hello
plugin system
Python"""
print("Third pipeline:")
pipeline3.display_pipeline()
print("Input:")
print(text3)
result3 = pipeline3.run(text3)
print("Final output:")
print(result3)

"""Plugin Pipeline
Abstract plugin system where new functionality is added without changing existing code
Build a plugin-based text processing system.

Abstract class: Plugin(ABC)
- Abstract methods: initialize(), execute(data), cleanup()
- Concrete method: get_name() — returns the class name

Concrete plugins:
- UppercasePlugin — converts all text to uppercase
- FilterPlugin(keyword) — removes lines containing the keyword
- SortPlugin(reverse=False) — sorts lines alphabetically
- NumberPlugin — prepends line numbers to each line
- UniquePlugin — removes duplicate lines

Pipeline class (NOT abstract — this is the runner):
- __init__() — holds a list of plugins
- add_plugin(plugin) — adds a plugin to the pipeline
- run(data) — calls initialize() on all plugins, then passes data through each plugin's execute() in sequence (output of one is input to next), then calls cleanup() on all. Returns final result.
- display_pipeline() — prints the ordered list of plugin names

Demonstrate:
1. Create a pipeline with: Uppercase → Sort → Number
2. Run it on a multi-line string (at least 6 lines)
3. Show the intermediate output after each plugin (print inside execute)
4. Create a DIFFERENT pipeline with: Filter("error") → Unique → Sort
5. Run it on different data
6. Show that adding a new plugin (e.g., ReversePlugin that reverses each line) requires ZERO changes to the Pipeline class

Example output:

Pipeline: UppercasePlugin → SortPlugin → NumberPlugin

Input:
banana
apple
cherry
apple
date

After UppercasePlugin: BANANA, APPLE, CHERRY, APPLE, DATE
After SortPlugin: APPLE, APPLE, BANANA, CHERRY, DATE
After NumberPlugin: 1. APPLE, 2. APPLE, 3. BANANA, 4. CHERRY, 5. DATE
"""