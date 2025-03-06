import os
import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


# 1. Target Interface: Defines the expected interface for data retrieval.
class DataProviderInterface(ABC):
    @abstractmethod
    def get_data(self) -> dict:
        pass


# 2. Adaptees: Existing classes with incompatible interfaces.
class JSONDataProvider:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_json(self) -> dict:
        with open(self.file_path, 'r') as f:
            return json.load(f)


class XMLDataProvider:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_xml(self) -> ET.ElementTree:
        tree = ET.parse(self.file_path)
        return tree


# 3. Adapters: Implement the Target Interface, using Adaptees to fulfill requests.
class JSONDataAdapter(DataProviderInterface):
    def __init__(self, json_provider: JSONDataProvider):
        self.json_provider = json_provider

    def get_data(self) -> dict:
        return self.json_provider.load_json()


class XMLDataAdapter(DataProviderInterface):
    def __init__(self, xml_provider: XMLDataProvider):
        self.xml_provider = xml_provider

    def get_data(self) -> dict:
        tree = self.xml_provider.parse_xml()
        root = tree.getroot()
        data = {}
        for element in root:
            data[element.tag] = element.text.strip()
        return data


# 4. Client: Uses the Target Interface to work with different data providers.
class DataAnalyzer:
    def __init__(self, data_provider: DataProviderInterface):
        self.data_provider = data_provider

    def analyze_data(self):
        data = self.data_provider.get_data()
        # Perform some actual analysis (e.g., calculate statistics, generate reports)
        print("Data Analysis:")
        for key, value in data.items():
            print(f"- {key}: {value}")


# Example Usage
def main():
    # 1. Instantiate Adaptees
    json_provider = JSONDataProvider("product.json")
    xml_provider = XMLDataProvider("product.xml")

    # 2. Wrap Adaptees with Adapters
    json_adapter = JSONDataAdapter(json_provider)
    xml_adapter = XMLDataAdapter(xml_provider)

    # 3. Inject Adapters into the Client
    json_analyzer = DataAnalyzer(json_adapter)
    xml_analyzer = DataAnalyzer(xml_adapter)

    # 4. Analyze data from different sources using the same client interface.
    print("Analyzing JSON data:")
    json_analyzer.analyze_data()

    print("\nAnalyzing XML data:")
    xml_analyzer.analyze_data()


if __name__ == "__main__":
    main()
