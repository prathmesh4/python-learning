from abc import ABC ,abstractmethod
import csv
import json
from io import StringIO

class DataExporter(ABC):
    @abstractmethod
    def export(self,data):
        """Export data and return as it a formatted string."""
        pass
    @abstractmethod
    def get_format(self):
        """Retrun the export format name."""
        pass   
    def validate(self,data):
        """Ensure data is a non-empty list of dictionaries."""
        if not isinstance(data,list) or not data:
            raise ValueError("Data must be a non-empty list.")
        if not all(isinstance(row,dict)for row in data):
            raise ValueError("Every item in data is must be a dictionary")
        headers =list(data[0].keys()) 
        if not headers:
            raise ValueError("Dictionaries must contain at least one key")
        if not all(list(row.keys()) == headers for row in data):
            raise ValueError("All dictionaries must have the same keys in the same order")
class CSVExporter(DataExporter):
    def get_format(self):
        return "CSV" 
    def export(self, data):
        output= StringIO()
        writer= csv.DictWriter(output,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        return output.getvalue().rstrip("\n")
class JSONExporter(DataExporter):
    def get_format(self):
        return "JSON"
    def export(self, data):
        return json.dumps(data,indent=2)
class MarkdownExporter(DataExporter):
    def get_format(self):
        return "Markdown"
    def export(self, data):
        headers = list(data[0].keys())
        rows=[
            [str(row[header]) for header in headers]
            for row in data
        ]
        widths=[
            max(len(str(header)), *(len(row[i]) for row in rows))
            for i,header in enumerate(headers)
        ]
        def format_row(values):
            return "| " + " | ".join(
                str(value).ljust(widths[i])
                for i,value in enumerate(values)
                ) +" |"
        header_row=format_row(headers)
        separator="|-" + "-|-".join(
            "-" * width for width in widths 
        ) + "-|"
        data_row=[format_row(row) for row in rows] 
        return "\n".join([header_row,separator,*data_row])
def export_data(data,exporter):
    exporter.validate(data)
    output =exporter.export(data)
    print(f"Format: {exporter.get_format()}")
    print(output)
    print()
students = [
    {"name": "Prathesh", "marks": 95, "city": "Mumbai"},
    {"name": "Pranav", "marks": 92, "city": "pune"},
    {"name": "Rahul", "marks": 67, "city": "Delhi"},
]    
exporters = [
    CSVExporter(),
    JSONExporter(),
    MarkdownExporter()
]

for exporter in exporters:
    export_data(students, exporter)