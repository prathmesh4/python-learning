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