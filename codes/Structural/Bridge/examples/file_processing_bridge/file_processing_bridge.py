from abc import ABC, abstractmethod
import os
import base64
import zlib
import json
from datetime import datetime


# Abstract Implementor
class FileHandler(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass

    @abstractmethod
    def write_file(self, file_path, content):
        pass


# Concrete Implementors
class TextFileHandler(FileHandler):
    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading text file: {e}")
            return None

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing text file: {e}")
            return False


class BinaryFileHandler(FileHandler):
    def read_file(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading binary file: {e}")
            return None

    def write_file(self, file_path, content):
        try:
            with open(file_path, 'wb') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing binary file: {e}")
            return False


# Abstraction
class FileProcessor(ABC):
    def __init__(self, handler: FileHandler):
        self.handler = handler

    @abstractmethod
    def process(self, source_path, target_path):
        pass


# Concrete Abstractions
class CompressingProcessor(FileProcessor):
    def process(self, source_path, target_path):
        print(f"Reading file: {source_path}")
        content = self.handler.read_file(source_path)

        if content is None:
            return False

        print("Compressing content...")
        if isinstance(content, str):
            compressed = zlib.compress(content.encode('utf-8'))
        else:
            compressed = zlib.compress(content)

        print(f"Writing compressed file: {target_path}")
        return self.handler.write_file(target_path, compressed)


class EncryptingProcessor(FileProcessor):
    def process(self, source_path, target_path):
        print(f"Reading file: {source_path}")
        content = self.handler.read_file(source_path)

        if content is None:
            return False

        print("Encrypting content (using base64 for demonstration)...")
        if isinstance(content, str):
            encrypted = base64.b64encode(content.encode('utf-8'))
        else:
            encrypted = base64.b64encode(content)

        print(f"Writing encrypted file: {target_path}")
        return self.handler.write_file(target_path, encrypted)


class LoggingProcessor(FileProcessor):
    def process(self, source_path, target_path):
        print(f"Reading file: {source_path}")
        content = self.handler.read_file(source_path)

        if content is None:
            return False

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "source_file": source_path,
            "target_file": target_path,
            "file_size": len(content) if content else 0
        }

        log_content = json.dumps(log_entry, indent=2)
        print(f"Creating log: {target_path}")
        print(f"Log content: {log_content}")

        return self.handler.write_file(target_path, log_content)


def create_sample_files():
    with open("sample_text.txt", "w", encoding="utf-8") as f:
        f.write("این یک فایل متنی نمونه است که شامل متن فارسی و انگلیسی است.\n")
        f.write("This is a sample text file with both English and Persian content.")

    binary_data = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]) + os.urandom(100)
    with open("sample_binary.bin", "wb") as f:
        f.write(binary_data)

    return "sample_text.txt", "sample_binary.bin"


def main():
    text_file, binary_file = create_sample_files()
    print(f"Created sample files: {text_file}, {binary_file}")

    text_handler = TextFileHandler()

    compressor = CompressingProcessor(text_handler)
    compressor.process(text_file, "compressed_text.bin")

    encryptor = EncryptingProcessor(text_handler)
    encryptor.process(text_file, "encrypted_text.bin")

    logger = LoggingProcessor(text_handler)
    logger.process(text_file, "text_file_log.json")

    binary_handler = BinaryFileHandler()

    compressor = CompressingProcessor(binary_handler)
    compressor.process(binary_file, "compressed_binary.bin")

    encryptor = EncryptingProcessor(binary_handler)
    encryptor.process(binary_file, "encrypted_binary.bin")

    logger = LoggingProcessor(binary_handler)
    logger.process(binary_file, "binary_file_log.json")

    print("\nFiles created:")
    for file in os.listdir("."):
        if os.path.isfile(file):
            print(f"- {file} ({os.path.getsize(file)} bytes)")


if __name__ == "__main__":
    main()
