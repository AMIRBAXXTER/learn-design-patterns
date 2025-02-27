from abc import ABC, abstractmethod
import json
import csv
from xml.dom import minidom


class FileHandler(ABC):

    @abstractmethod
    def save(self, data, file_path):
        pass

    @abstractmethod
    def load(self, file_path):
        pass


class JsonFileHandler(FileHandler):

    def __init__(self, indent=4):
        self.indent = indent

    def save(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=self.indent)
        print(f'Data saved {file_path}')

    def load(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        print(f'Data loaded from {file_path}')
        return data


class XmlFileHandler(FileHandler):

    def __init__(self, indent=4, encoding='utf-8', standalone=True):
        self.indent = indent
        self.encoding = encoding
        self.standalone = standalone

    def save(self, data, file_path):
        root = minidom.Document()

        root_element = root.createElement('data')
        root.appendChild(root_element)

        for key, value in data.items():
            child = root.createElement(key)
            child.appendChild(root.createTextNode(str(value)))
            root_element.appendChild(child)

        xml_bytes = root.toprettyxml(indent=' ' * self.indent, encoding=self.encoding)
        xml_string = xml_bytes.decode(self.encoding)
        declaration = f'<?xml version="1.0" encoding="{self.encoding}" standalone="{'yes' if self.standalone else 'no'}"?>\n'
        xml_string = declaration + xml_string.split('\n', 1)[1]
        with open(file_path, 'w', encoding=self.encoding) as file:
            file.write(xml_string)
        print(f'Data saved {file_path}')

    def load(self, file_path):
        dom = minidom.parse(file_path)
        data = {child.nodeName: child.firstChild.nodeValue for child in dom.documentElement.childNodes if
                child.nodeType == minidom.Node.ELEMENT_NODE}
        dom.unlink()
        print(f'Data loaded from {file_path}')
        return data


class CsvFileHandler(FileHandler):

    def __init__(self, delimiter=',',  quotechar='"'):
        self.delimiter = delimiter
        self.quotechar = quotechar

    def save(self, data, file_path):
        data = [data] if isinstance(data, dict) else data
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            data = [dict(zip(data[0].keys(), item.values())) for item in data]
            with open(file_path, 'w') as file:
                writer = csv.DictWriter(file, data[0].keys(), delimiter=self.delimiter, quotechar=self.quotechar)
                writer.writeheader()
                writer.writerows(data)
            print(f'Data saved {file_path}')
        else:
            raise ValueError('data must be a list of dicts')

    def load(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file, delimiter=self.delimiter, quotechar=self.quotechar)
            data = [dict(row) for row in reader]
        print(f'Data loaded from {file_path}')
        return data


class FileHandlerFactory:

    @abstractmethod
    def create_file_handler(self):
        pass


class JsonFileHandlerFactory(FileHandlerFactory):

    def __init__(self, indent=4):
        self.indent = indent

    def create_file_handler(self):
        return JsonFileHandler(indent=self.indent)


class XmlFileHandlerFactory(FileHandlerFactory):

    def __init__(self, indent=4, encoding='utf-8', standalone=True):
        self.indent = indent
        self.encoding = encoding
        self.standalone = standalone

    def create_file_handler(self):
        return XmlFileHandler(indent=self.indent, encoding=self.encoding, standalone=self.standalone)


class CsvFileHandlerFactory(FileHandlerFactory):

    def create_file_handler(self):
        return CsvFileHandler()


def main():
    data = {'name': 'amir', 'age': 27, 'city': 'Fardis'}

    json_factory = JsonFileHandlerFactory(indent=8)
    json_handler = json_factory.create_file_handler()
    json_handler.save(data, 'data.json')
    print(f'Loaded Json data: {json_handler.load("data.json")}')

    xml_factory = XmlFileHandlerFactory(indent=8, standalone=False)
    xml_handler = xml_factory.create_file_handler()
    xml_handler.save(data, 'data.xml')
    print(f'Loaded Xml data: {xml_handler.load("data.xml")}')

    csv_factory = CsvFileHandlerFactory()
    csv_handler = csv_factory.create_file_handler()
    csv_handler.save(data, 'data.csv')
    print(f'Loaded Csv data: {csv_handler.load("data.csv")}')


if __name__ == "__main__":
    main()
